import sys
import os
import logging    
import time
import traceback
from waveshare_OLED import OLED_1in5_rgb
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)

class Oled():
    def __init__(self):
        try:
            self.disp = OLED_1in5_rgb.OLED_1in5_rgb()

            logging.info("\r 1.5inch rgb OLED ")
            # Initialize library.
            self.disp.Init()
            # Clear display.
            logging.info("clear display")
            self.disp.clear()
        except IOError as e:
            logging.info(e)

    def __del__():
        self.disp.module_exit()

    def display(self, speed):

        self.disp.clear()

        try:
            logging.info ("***draw image")
            Himage2 = Image.new('RGB', (self.disp.width, self.disp.height), 0)  # 0: clear the frame
            png = Image.open(os.path.join('pic', f'speed-{speed}.png'))
            Himage2.paste(png.resize((self.disp.width-20, self.disp.height-20)), (10,10))
            Himage2=Himage2.rotate(0) 	
            self.disp.ShowImage(self.disp.getbuffer(Himage2)) 
            time.sleep(10)    
        except IOError as e:
            logging.info(e)
            
    def clear(self):
        self.disp.clear()