#!/usr/bin/env python2

import json
import os
import time
import requets
import sys

print ("Jadwal Sholat Dunia")
print 
pri = input("\033[98mMasukan nama negara =>> ")
ezz = input("\033[37;1mMasukan nama kota negara ==>> ")
        r = requests.get('https://www.islamicfinder.org/world/"+pri"/"+ezz"-prayer-times/?language=id') 

print ("Dzuhur >", r.json()["data"]["Dzuhur"]) 
print ("MAGHRIB >", r.json()["data"]["Maghrib"]) 
print ("Maghrib >", r.json()["data"]["Maghrib"]) 
print ("ISHA >", r.json()["data"]["Isha"]) 
print ("\033[00m")
os.system("exit")