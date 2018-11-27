import time

from statslib import cpu

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi hardware SPI config:
#DC = 23
#RST = 24
#SPI_PORT = 0
#SPI_DEVICE = 0

SCLK = 11
DIN = 10
DC = 23
RST = 24
CS = 8

#software spi
disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)


# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

while True:
    # clear screen
    #disp.clear()
    #disp.display()
    # Write some text.
    #draw.text((8,30), 'CPU ' + cpu(), font=font)
    # Display image.
    #disp.image(image)
    draw.text((1,30), 'cpu: ' + cpu(), font=font)
    disp.clear()
    disp.image(image)
    disp.display()
    time.sleep(1)

print 'Press Ctrl-C to quit.'
while True:
	time.sleep(1.0)
