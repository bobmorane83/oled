import sys
import os
import logging    
import time
import traceback
from waveshare_OLED import OLED_1in5_rgb
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)

try:
    disp = OLED_1in5_rgb.OLED_1in5_rgb()

    logging.info("\r 1.5inch rgb OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()

    logging.info ("***draw image")
    Himage2 = Image.new('RGB', (disp.width, disp.height), 0)  # 0: clear the frame
    png = Image.open(os.path.join('signs/pic', 'speed-80.png'))
    Himage2.paste(png.resize((disp.width-20, disp.height-20)), (10,10))
    Himage2=Himage2.rotate(0) 	
    disp.ShowImage(disp.getbuffer(Himage2)) 
    time.sleep(10)    

    disp.clear()

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    disp.module_exit()
    exit()