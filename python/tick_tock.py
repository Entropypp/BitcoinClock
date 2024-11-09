#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
lib_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(lib_dir):
	sys.path.append(lib_dir)

import logging
from waveshare_epd import epd2in13_V4
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

import json 
import requests 
  
# defining key/request url 
key = 
  
# requesting data from url 
try:
	btcusd = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()['price']
except Exception as e:
	logging.info(e)
	exit

try:
	logging.debug("Using epd2in13_V4")
	epd = epd2in13_V4.EPD()
	logging.debug("Font: Retrospect.ttf (120)")
	font = ImageFont.truetype(os.path.join(font_dir, 'Retrospect.ttf'), 120)

	image = Image.new('1', (epd.height, epd.width), 255)
	draw = ImageDraw.Draw(image)

	epd.init_fast()
	draw.rectangle((0, 0, epd.height, epd.width), fill = 255)
	draw.text((5, 5),"${}".format(btcusd), font = font, fill = 0)
	epd.display_fast(epd.getbuffer(image.rotate(180)))
	epd.sleep()

		
except IOError as e:
	logging.info(e)
	
except KeyboardInterrupt:	
	logging.info("ctrl + c:")
	epd2in13_V4.epdconfig.module_exit(cleanup=True)
	exit()
