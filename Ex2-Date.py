# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 11:48:51 2019

@author: mina2
"""

import datetime

class Date:
    
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
        
    def getDate(self):
        try:
            date = datetime.datetime(self.year, self.month, self.day)
            return date.strftime("%b %d %Y")
        except:
            print('Invalide Date')