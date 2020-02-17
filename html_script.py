#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:55:20 2020

@author: bitlucky
"""

import os
import time
import requests
import sys 

def retrieve_html():
    for year in range(2013 , 2019):
        for month in range(1 , 13):
            if(month<10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month , year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month , year)
        source_text = requests.get(url)
        text_utf = source_text.text.encode('utf=8')
        
        if not os.path.exists("/Data/Html_Data/{}".format(year)):
            os.makedirs("/Data/Html_Data/{}".format(year))
        with open("/Data/Html_Data/{}/{}.html".format(year,month), "wb") as output:
            output.write(text_utf)
        
        sys.stdout.flush()
        
if __name__ = "__main__":
    start_time=time.time()
    retrieve_html()
    stop_time = time.table()
    print("Time taken {}".format(stop_time - start_time))