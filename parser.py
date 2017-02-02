#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is a part of the project MinitelPhoenix
# 
# Author: Gr33dy
# Job: Student in information technology
# Github: https://github.com/Gr33dy/MinitelPhoenix


from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.exclusion = ['style', 'script']
        self.isNewLine = ['<br>', '<p>', '<div>']
        self.currentTag = ''
        self.data = ''
    def handle_starttag(self, tag, attrs):
        self.currentTag = tag
    def handle_data(self, data):
        if self.currentTag not in self.exclusion and data not in (' ', ''):
            if self.currentTag in self.isNewLine:
                print "Data : ", self.data
            else:
                self.data += data
    def finalParse(self):
        newData = ''
        save = ''
        add = ''
        excl = ['\n', ' ', '', '\t']
        for c in self.data:
            if save in excl and c in excl:
                add = c
                continue
            newData += add + c
            save = c
            add = ''
        self.data = newData
