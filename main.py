#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is a part of the project MinitelPhoenix
# 
# Author: Gr33dy
# Job: Student in information technology
# Github: https://github.com/Gr33dy/MinitelPhoenix


import sys
import time
from minitel import Minitel
from minitel_tools import *
from wifi_minitel import Wifi
from services import Services

if __name__ == '__main__':
    print('START - ' + time.strftime("%d-%m-%Y %H:%M"))
    m = Minitel('/dev/ttyUSB0')
    w = Wifi()
    header(m)
    if not w.isConnected():
        connected = False
        while not connected:
            w.printSsids(m)
            w.selectSsid(m)
            w.getPasskey(m)
            connected = w.connexion(m)

    s = Services(m)
    while True:
        s.getService()
        s.interpreter()
        
