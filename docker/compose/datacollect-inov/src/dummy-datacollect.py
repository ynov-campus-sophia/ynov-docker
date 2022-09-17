#!/usr/bin/python
import krakenex
import json
import sys
from pykrakenapi import KrakenAPI
api = krakenex.API()
k = KrakenAPI(api)
import datetime
import schedule
import time
import logging
import os
from flask import Flask, request

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/fetch', methods=['GET'])
def fetch():
   args=request.args
   print(args.to_dict())
   pair = args.get('pair')
   return job(pair)

def job(pair):
    logging.info("Fetching data")
    try:
        ohlc, last = k.get_ohlc_data(pair)
        logging.info('pair: %s',pair)
        logging.info(ohlc)
        return ohlc.to_json()
    except:
        logging.error("Unexpected error while fetching data for {}: {}", pair, sys.exc_info()[0])
            
        

app.run(debug=True, host='0.0.0.0')
