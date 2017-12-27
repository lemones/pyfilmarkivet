#!/bin/bash

u="$(python ./main.py old | grep -Po '(?<=href=")*http://www.filmarkivet.se/movies*[^"]*')"
echo $u | tr " " "\n" | awk -F / '{ print $(NF-1) }'
