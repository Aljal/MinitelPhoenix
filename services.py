#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is a part of the project MinitelPhoenix
# 
# Author: Gr33dy
# Job: Student in information technology
# Github: https://github.com/Gr33dy/MinitelPhoenix


from minitel_tools import *
from parser import Parser
from bs4 import BeautifulSoup
import requests
import json

class Services:
    def __init__(self, m):
        self.service = ''
        self.minitel = m
        self.server = 'http://minitel-phoenix.herokuapp.com/api/'
        return

    def getService(self):
        header(self.minitel)
        renderText(self.minitel, {'x':5,'y':5,'text':'Choose a service or enter an URL :'})
        services = self.getServices('services')
        i = 0
        while i < len(services):
            renderText(self.minitel, {'x':5,'y':6 + i,'text':services[i]})
            i = i + 1
        renderText(self.minitel, {'x':5,'y':6 + i + 1,'text':'Service or URL : '})
        self.service = readUntil(self.minitel, 'Envoi')
        self.service = self.service.lower()
        print '[+] Service : ' + self.service

    def interpreter(self):
        if self.service[0:4] == '3615':
            self.getServiceProvider()
        else:
            ret = self.getWebsiteContent()
            return ret

    def getContent(self, url):
        try:
            r = requests.get(url)
            print '[+] Response : ' + str(r.status_code)
            parser = Parser()
            soup = BeautifulSoup(r.text, 'html.parser')
            parser.feed(soup.prettify())
            parser.finalParse()
            data = parser.data
            return data
        except Exception as e:
            print '[-] Error : URL not found'
            renderText(self.minitel, {'x':5,'y':15,'text':'Error : URL not found'})
            return False

    def getLine(self, data):
        tab = list()
        line = ''
        i = 0
        for c in data:
            line = line + c
            i = i + 1
            if c == '\n' or i % 35 == 0:
                tab.append(line)
                line = ''
        return tab

    def getWebsiteContent(self):
        url = ''
        if self.service[0:7] != 'http://' and self.service[0:8] != 'https://':
            url = 'http://'
        url += self.service
        data = self.getContent(url)
        if data == False:
            return False
        data = self.getLine(data)
        i = 0
        while True:
            header(self.minitel)
            j = 0
            while j < 19:
                try:
                    renderText(self.minitel, {'x':5,'y':5 + j,'text':data[(i + 1) * j]})
                except:
                    pass
                j = j + 1
            user = navigate(self.minitel)
            print 'User : ' + user
            if user == 'next' and i < (len(data) - 1):
                i = i + 1
            if user == 'previous' and i > 0:
                i = i - 1
            if user == 'quit':
                return True

    def getServices(self, param):
        r = requests.get(self.server + param)
        result = json.loads(r.text)
        result = result['message']
        return result

    def getServiceProvider(sefl):
        print '[-] Warning: ' + self.service + ' is not implemented, any services are implemented in fact because the api developpement stopped :p'
        renderText(self.minitel, {'x':5,'y':15 + j,'text':'The service: ' + self.service + ' is not implemented']})
        
