#!/bin/bash

u="$(python ./all.py | grep -Po '(?<=href=")*http://www.filmarkivet.se/movies*[^"]*')"
# echo $u | tr " " "\n"
echo $u | tr " " "\n" | awk -F / '{ print $(NF-1) }'
