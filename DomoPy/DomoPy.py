#!/usr/bin/env python3=
# -*- coding: utf-8 -*-

import requests
import json
import sys


class DomoPy:
    """

    Simple class to use the Domoticz JSON API.
    Only tested with basic auth for the moment

    """

    def __init__(self, domoticz_IP='', domoticz_port='', domoticz_user='', domoticz_password='' ):
        self.domoticz_IP = domoticz_IP
        self.domoticz_port = domoticz_port
        self.domoticz_user = domoticz_user
        self.domoticz_password = domoticz_password
        return

    def __repr__(self):
        return "Domoticzpi: IP({}), port({}), user({}), password({})".format(
                self.domoticz_IP, self.domoticz_port, self.domoticz_user, self.domoticz_password)

    def __Requests(self, command):
        ## Domoticz / Setup / Settings / Security / API Protection : Allow Basic-Auth authentication over plain HTTP (API only)
        r = requests.get(f"http://{self.domoticz_IP}:{self.domoticz_port}/json.htm?type=command&param=" + command, auth=(self.domoticz_user,self.domoticz_password), verify=True)
        if r.status_code == 200:
            j=json.loads(r.text)
        else:
            print ('HTTP Error : ' + str(r.status_code))
            sys.exit(2)
        return(j)

    def getTemp(self):
        j=self.__Requests('getdevices&filter=temp&used=true&order=Name')
        return j['result']

    def getLight(self):
        j=self.__Requests('getdevices&filter=light&used=true&order=Name')
        return j['result']

    def getWeather(self):
        j=self.__Requests('getdevices&filter=weather&used=true&order=Name')
        for dev in j['result']:
            print (dev['Name'] + ' : ' + dev['Data'])

    def getUtility(self):
        j=self.__Requests('getdevices&filter=utility&used=true&order=Name')
        return j['result']

    def getLightSwitchesNames(self):
        j=self.__Requests('getdevices&filter=light&used=true&order=Name')
        return j['result']

    def getVersion(self):
        j=self.__Requests('getversion')
        #return j['version']
        for dev in j:
            print (f'Have Update? {dev['HaveUpdate']}')
            print (f'Version    : {dev['version']}')
            print (f'Status     : {dev['status']}')
            return j['HaveUpdate'], j['version'], j['status']

    def getStatus(self):
        j=self.__Requests('getversion')
        return j['status']
    
    def getSunrise(self):
        j=self.__Requests('getSunRiseSet')
        return j['Sunrise']

    def getSunset(self):
        j=self.__Requests('getSunRiseSet')
        return j['Sunset']
