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

try:
    logging.info("Using epd2in13_V4")
    
    epd = epd2in13_V4.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
    
    # Drawing on the image
    font = ImageFont.truetype(os.path.join(font_dir, 'Pixel-lcd-machine.ttf'), 100)
    
    logging.info("E-paper refresh")

    logging.info("E-paper refreshes quickly")
    epd.init_fast()
    logging.info("1.Drawing on the image...")
    for i in range(75000,75123,22):
        image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
        draw = ImageDraw.Draw(image)
        draw.text((5, 5),str(i), font = font, fill = 0)
        epd.display_fast(epd.getbuffer(image))
        time.sleep(5)
        
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
