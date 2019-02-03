#!/usr/bin/env python2 


import json
import requests
import os 
import time 
import sys
 
print
time.sleep(1)
print ("\033[97mJadwal Sholat Lokal")
print
dcok = raw_input("\033[00mMasukkan Kota => ") 
r = requests.get('https://time.siswadi.com/pray/"+dcok"') 
print ("\033[31;1m")
print ("ASAR >", r.json()["data"]["Asr"]) 
print ("MAGHRIB >", r.json()["data"]["Maghrib"]) 
print ("ISHA >", r.json()["data"]["Isha"]) 
print ("SEPERTIGA MALAM >",r.json()["data"]["SepertigaMalam"]) 
print ("TENGAH MALAM >", r.json()["data"]["TengahMalam"]) 
print ("DUAPERTIGAMALAM >", r.json()["data"]["DuapertigaMalam"]) 
print ("SUBUH >", r.json()["data"]["Fajr"]) 
print ("SUNRISE >", r.json()["data"]["Sunrise"]) 
print ("\033[00m")
os.system("exit")