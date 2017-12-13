#!/bin/python
'''
prints everything inside <div class=video-container>...</div
'''
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Must have arg")
    exit()

# U = 'http://www.filmarkivet.se/movies/langs-vagen/'
U = sys.argv[1]
SRC = urlopen(U)
SOUP = BeautifulSoup(SRC, "html5lib")

LIST = SOUP.find_all('div', class_='video-container')
print(LIST)
