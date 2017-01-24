import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "html.parser")
    return soupdata

playerdatasaved = " "
for letter in ascii_lowercase:
    soup = make_soup("http://www.basketball-reference.com/players/" + letter + "/")
for record in soup.findAll('tr'):
    playerdata = ""
    for data in record.findAll('td'):
        playerdata = playerdata+","+data.text
    playerdatasaved = playerdatasaved + "\n" + playerdata[1:]

header = "Player,From,To,Pos,Ht,Wt,Birth Date,College" + "\n"
file = open(os.path.expanduser("Basketballtable.csv"),"wb")
file.write(bytes(header, encoding="ascii",errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii",errors='ignore'))

