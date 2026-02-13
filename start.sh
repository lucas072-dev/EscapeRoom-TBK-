#!/bin/bash

trap '' INT
stty -echoctl

python3 /home/pi/Escaperoom-tbk-/app.py
