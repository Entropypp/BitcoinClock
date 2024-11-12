#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
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
  
  




def get_btc_usd():
	try:
		response  = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
		btc_usd = response.json()
		return "${}".format(round(float(btc_usd['price'])))
	except Exception as e:
		logging.info(e)
		return 0

def get_font(font_name,max_width,text_string):
	font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
	font_size = 10
	width = 0
	while width<max_width:
		font = ImageFont.truetype(os.path.join(font_dir, font_name), font_size)
		width = font.getmask(text_string).getbbox()[2]
		font_size = font_size+1 if width<max_width else font_size
	return ImageFont.truetype(os.path.join(font_dir, font_name), font_size)

def epaper_btc_price():
	try:
		epd = epd2in13_V4.EPD()
		btc_string = get_btc_usd()
		font = get_font('Retrospect.ttf',epd.height-10,btc_string)
		epd.init_fast()
		image = Image.new('1', (epd.height, epd.width), 255)
		draw = ImageDraw.Draw(image)
		draw.rectangle((0, 0, epd.height, epd.width), fill = 255)
		draw.text((5, 5),btc_string, font = font, fill = 0)
		epd.display_fast(epd.getbuffer(image.rotate(180)))
		epd.sleep()

	except Exception as e:
		logging.info(e)
		epd2in13_V4.epdconfig.module_exit(cleanup=True)
		return False
		
	return True

####Main		
epaper_btc_price()