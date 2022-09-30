# tigattack's CarPi Setup

### [ansible](/ansible/)

This directory contains an Ansible playbook to provision the Pi from a stock install of OpenAuto.

### [pi](/pi/)

This directory contains all files to be used on the Pi. See further details in [pi/README.md](pi/README.md).

---

## Kit List

Also see [OpenAuto required hardware](https://bluewavestudio.io/community/thread-2183.html).

| Item                               | Notes                                                                                                                                                                               | Link                                                                                                                                |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Raspberry Pi 4B 4GB                | [RPiLocator](https://rpilocator.com/) is a great source for finding stock.                                                                                                          | https://thepihut.com/products/raspberry-pi-4-model-b?variant=20064052740158                                                         |
| SanDisk Extreme 32GB Micro SD card | Class 10, U3 is recommended by OpenAuto.                                                                                                                                            | https://amzn.to/3LY07ZK (Affiliate link)                                                                                                           |
| 7” touchscreen                     | IPS, capacitive touch, 1024×600. [Wiki page](https://www.waveshare.com/wiki/7inch_HDMI_LCD_(C)).                                                                                    | https://thepihut.com/collections/touchscreen-displays-for-raspberry-pi/products/7-ips-capacitive-touchscreen-lcd-low-power-1024x600 |
| Bluetooth USB adaptor              | Must be non-Broadcom. CSR8510 A10 chip is recommended.                                                                                                                              | https://amzn.to/3BPQdol (Affiliate link)                                                                                                           |
| USB-3.5mm audio adaptor            | **Not final.** Just used for testing right now.                                                                                                                                     | https://thepihut.com/products/usb-audio-adapter-works-with-raspberry-pi                                                             |
| Microphone 3.5mm                   |                                                                                                                                                                                     | https://amzn.to/33XulXy (Affiliate link)                                                                                                           |
| Single-channel CAN HAT             | There is also a [Dual-channel CAN HAT](https://thepihut.com/products/2-channel-isolated-can-hat-for-raspberry-pi) which is a good idea if you want to connect to more than one bus. | https://thepihut.com/products/rs485-can-hat-for-raspberry-pi                                                                        |
| USB GPS module                     | Improves GPS and saves phone battery when using AA. Unsourced so far.                                                                                                               |                                                                                                                                     |
| RTC                                |                                                                                                                                                                                     | https://thepihut.com/products/mini-rtc-module-for-raspberry-pi                                                                      |
| DC/DC converter                    | Zero2Go Omini rev2. [PDF manual](https://www.uugear.com/doc/Zero2Go_Omini_UserManual.pdf).                                                                                          | https://thepihut.com/products/zero2go-omini-rev2-wide-input-range-power-supply                                                      |
| M2.5 12mm standoff pack            | For HAT stacking.                                                                                                                                                                   | https://thepihut.com/products/m2-5-nylon-standoff-packs?variant=41056882360515                                                      |
| M2.5 5mm screw pack                | To go with the standoffs above.                                                                                                                                                     | https://thepihut.com/products/m2-5-nylon-fixing-packs?variant=41056997081283                                                        |
| GPIO stacking header               | For HAT stacking.                                                                                                                                                                   | https://thepihut.com/products/gpio-stacking-header-for-pi-a-b-pi-2-pi-3                                                             |
| JST-XH compatible cable            | For power supply input.                                                                                                                                                             | https://thepihut.com/products/2-5mm-pitch-2-pin-cable-matching-pair-jst-xh-compatible                                               |
