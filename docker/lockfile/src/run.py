#!/usr/bin/python3
import logging
from flask import Flask, request

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Ynov Hello World'

app.run(debug=True, host='0.0.0.0')
