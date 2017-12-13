#!/bin/bash

u="$(python ./main.py $1 | awk '/mp4/ {print $2}' | awk -F'rtmp' '{print $1}' | sed -n 3p)"
echo $u
