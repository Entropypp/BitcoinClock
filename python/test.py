#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
lib_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V4
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Using epd2in13_V4")
    
    epd = epd2in13_V4.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
	
    # Drawing on the image
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Janky.ttf'), 24)
    
	logging.info("E-paper refresh")

	logging.info("E-paper refreshes quickly")
	epd.init_fast()
	logging.info("1.Drawing on the image...")
	image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
	draw = ImageDraw.Draw(image)
    for i in range(75000,75123,25):
		draw.text((110, 90),i, font = font24, fill = 0)
		epd.display_fast(epd.getbuffer(image))
		time.sleep(2)
        
    logging.info("Clear...")
    epd.init()
    epd.Clear(0xFF)
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V4.epdconfig.module_exit(cleanup=True)
    exit()
