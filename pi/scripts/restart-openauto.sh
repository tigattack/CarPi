#!/bin/bash

pkill openauto

DISPLAY=:0 nohup /usr/bin/stdbuf -o0 /usr/local/bin/autoapp > /home/pi/.openauto/cache/openauto.log &
