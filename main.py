#!/bin/python
'''
prints everything inside <a href"*">
'''
import sys
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Accepted arguments: all, url, old, get [URL]")
    exit()

U = 'http://www.filmarkivet.se/filmer-a-o/'
SRC = urlopen(U)
SOUP = BeautifulSoup(SRC, "html5lib")


# No current usage
if sys.argv[1] == "all":
    PRU = SOUP.find('ul', attrs={"class": "alphabetical"})
    for link in PRU.find_all_next('a'):
        print(link.get('href'))
    print("Results: %s" % len(PRU))

# Print all links that contains /movies/
elif sys.argv[1] == "url":
    PRU = SOUP.find_all('a', href=re.compile("/movies/"))
    for i in PRU:
        print("%s" % i)
    print("Results: %s" % len(PRU))

# For use with Shell script
elif sys.argv[1] == "old":
    PRU = SOUP.find_all('a', href=True)
    print("%s" % PRU)

# Print mp4 link of given url (not complete. Use shell script)
elif sys.argv[1] == "get":
    if len(sys.argv) < 3:
        print("Must contain URL")
        exit()
    U = sys.argv[2]
    SRC = urlopen(U)
    SOUP = BeautifulSoup(SRC, "html5lib")
    PRU = SOUP.find_all('div', class_='video-container')
    print("%s" % PRU)

else:
    print("Accepted arguments: all, url, old, get [URL]")
    exit()
