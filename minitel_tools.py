#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is a part of the project MinitelPhoenix
# 
# Author: Gr33dy
# Job: Student in information technology
# Github: https://github.com/Gr33dy/MinitelPhoenix


import minitel
import time

DICT = {'A':'Envoi',
        'B':'Retour',
        'C':'Repetition',
        'D':'Guide',
        'E':'Annulation',
        'F':'Sommaire',
        'G':'Correction',
        'H':'Suite',
        'Y':'Connexion'}


def renderText(m, e):
    x = e.get('x',0) # Horizontal coordinate (abscissa) of the beginning of the message
    y = e.get('y',0) # Vertical coordinate (ordinate) of the beginning of the message
    text = e.get('text','') # Message text
    fg = e.get('fg',7) # Forground color
    bg = e.get('bg',0) # Background color
    m.moveCursor(x,y)
    m.setVTMode(minitel.VT_TEXT)
    m.setColors(fg,bg)
    m.send(text)

def header(m):
        m.clearScreen()
        renderText(m, {'x':5,'y':0,'text':' EPITECH - Minitel Phoenix ','fg':0,'bg':5})

def readOne(m): # We use "while True" because the function recv() is a non blocking read
    while True:
        key = m.recv(1)
        if key != '' and type(key) == str:
            return key
        time.sleep(0.1)

def shortCuts(m, expect):
    key = readOne(m)
    if ord(key) == 19:
        key = m.recv(1)
        try:
            return True if expect == DICT[key] else False
        except:
            return False

def readUntil(m, expect):
    msg = ''
    key = ''
    while True:
        key = readOne(m)
        if ord(key) == 19:
            break
        msg = msg + key
    key = m.recv(1)
    try:
        print DICT[key]
        if DICT[key] == expect:
            return msg
        while not shortCuts(m, expect):
            pass # Or print a text to say to the user that he need to press "expect" key
        return msg
    except:
        return False

def clearLine(m, y):
    renderText(m, {'x':0,'y':y,'text':'                                        '})

def navigate(m):
    key = readOne()
    if key == 'N':
        return 'next'
    if key == 'P':
        return 'previous'
    if key == 'Q':
        return 'quit'
    
