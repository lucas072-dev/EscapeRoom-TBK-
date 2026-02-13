#!/bin/bash

trap '' INT
stty -echoctl

python3 test.py
