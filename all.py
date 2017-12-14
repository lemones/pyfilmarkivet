#!/bin/python
'''
prints everything inside <a href"*">
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

U = 'http://www.filmarkivet.se/filmer-a-o/'
SRC = urlopen(U)
SOUP = BeautifulSoup(SRC, "html5lib")

LIST = SOUP.find_all('a', href=True)
print(LIST)
