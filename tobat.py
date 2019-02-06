#!/usr/bin/env python2 
#-*- coding: utf-8 -*-
"""
# mau ngapain exploit nano? 
# heleh w nuub stah^_^
# hae
"""

sholat= """\033[97m
____  _           _       _
/ ___|| |__   ___ | | __ _| |_
\___ \| '_ \ / _ \| |/ _` | __|
 ___) | | | | (_) | | (_| | |_
|____/|_| |_|\___/|_|\__,_|\__|

\033[92mTools buat tobat gan^-^

\033[91mBerfaedah Banget ^~^

\033[00mAuthor : StarFuckTak

\033[96mPress Vol (-) + z to exit
"""

import os 
import time 
import sys
 
os.system("clear") 

print sholat

print "\033[35;1m"
print ("____________________________________")
print ("[ 1. ] Untuk Lokal")
print ("[ 2. ] Untuk Dunia")
print ("[ 0. ] Exit ")
print ("____________________________________\033[00m")
time.sleep(1)
bntng = input("\033[00mRoot@localhost => ") 

if bntng == 1:
           os.system("clear")
           time.sleep(0.1)
           os.system("python2 lokal.py")
           os.system("exit")

if bntng == 2:
         time.sleep(0.1)
         os.system("python2 world.py")
         os.system("exit")

if bntng == 0:
        os.system('clear')
        os.system("echo good luck | lolcat")
        time.sleep(2)
        os.system("exit")

else:
        print ("\033[93mwrong input")
        time.sleep(0.5)
        system.exit()
