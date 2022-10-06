#
#  Copyright (C) BlueWave Studio - All Rights Reserved
#
# Modified by Jon LaBass for CPU temperature monitoring
# https://bluewavestudio.io/community/thread-3314.html
# Further modified by tigattack to improve formatting and
# make fit for use case.
#

import os
import threading

import common.Api_pb2 as oap_api
from common.Client import Client, ClientEventHandler
from gpiozero import CPUTemperature

# Define cpu threshold (*C)
CPU_THRESHOLD = 60

cpu = CPUTemperature()

class EventHandler(ClientEventHandler):

    def __init__(self):
        self._notification_channel_id = None
        self._timer = None

    def on_hello_response(self, client, message):
        print((f"received hello response, result: {message.result}," +
                f"oap version: {message.oap_version.major}.{message.oap_version.minor}," +
                f"api version: {message.api_version.major}.{message.api_version.minor}")
            )

        register_notification_channel_request = oap_api.RegisterNotificationChannelRequest(
        )
        register_notification_channel_request.name = "Power Management Notification Channel"
        register_notification_channel_request.description = (
            "Notification channel for power management alerts"
        )

        client.send(oap_api.MESSAGE_REGISTER_NOTIFICATION_CHANNEL_REQUEST, 0,
                    register_notification_channel_request.SerializeToString())

    def on_register_notification_channel_response(self, client, message):
        print(
            (f"register notification channel response, result: {message.result}," +
            f"icon id: {message.id}")
        )
        self._notification_channel_id = message.id

        if message.result == (
                oap_api.RegisterNotificationChannelResponse.REGISTER_NOTIFICATION_CHANNEL_RESULT_OK
            ):
            print("notification channel successfully registered")
            self.show_notification(client)

    def show_notification(self, client):
        cpu_temperature = cpu.temperature
        if cpu_temperature > CPU_THRESHOLD:
            cpu_temp_format = str(round(cpu_temperature,1))+'\N{DEGREE SIGN}'+'C'
            print("sending notification")

            show_notification = oap_api.ShowNotification()
            show_notification.channel_id = self._notification_channel_id
            show_notification.title = "CPU Temperature Alert"
            show_notification.description = "CPU temperature is "+cpu_temp_format
            show_notification.single_line = "CPU Temp - "+cpu_temp_format

            with open("assets/notification_icon.svg", 'rb') as icon_file:
                show_notification.icon = icon_file.read()

            with open("assets/notification_sound.wav", 'rb') as sound_file:
                show_notification.sound_pcm = sound_file.read()

            client.send(oap_api.MESSAGE_SHOW_NOTIFICATION, 0,
                    show_notification.SerializeToString())

            self._timer = threading.Timer(60, self.show_notification, [client])
            self._timer.start()

    def get_notification_channel_id(self):
        return self._notification_channel_id

    def get_timer(self):
        return self._timer


def main():
    client = Client("cpu temp notification")
    event_handler = EventHandler()
    client.set_event_handler(event_handler)
    client.connect('127.0.0.1', 44405)

    active = True
    while active:
        try:
            active = client.wait_for_message()
        except KeyboardInterrupt:
            break

    if event_handler.get_timer() is not None:
        event_handler.get_timer().cancel()

    if event_handler.get_notification_channel_id() is not None:
        unregister_notification_channel = oap_api.UnregisterNotificationChannel(
        )
        unregister_notification_channel.id = event_handler.get_notification_channel_id(
        )
        client.send(oap_api.MESSAGE_UNREGISTER_NOTIFICATION_CHANNEL, 0,
                    unregister_notification_channel.SerializeToString())

    client.disconnect()


if __name__ == "__main__":
    main()
