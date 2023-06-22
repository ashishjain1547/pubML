# Code for Python 2.6

import urllib2
from urllib2 import URLError
import json
from time import sleep, strftime
import logging
import datetime

def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        response = urllib2.urlopen(URL)
        data = json.load(response)         
        priceFloat = float(data['last']) #Lastprice
        
        priceDate = datetime.datetime.fromtimestamp(int(data['timestamp'])).strftime('%d/%m/%Y')
        priceTime = datetime.datetime.fromtimestamp(int(data['timestamp'])).strftime('%H:%M:%S')

        return str(priceDate + "," + priceTime + "," + str(priceFloat))
    except URLError, e:
        print("Error querying Bitstamp API: ", e.reason)

LOG_FILENAME = 'BTC.csv'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format='%(message)s')

logging.debug("Date,Time,USD/BTC")
while True:
    logging.debug(str(getBitcoinPrice()))
    sleep(20)
