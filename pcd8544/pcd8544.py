import math
import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from statslib  import cpu
from gpiozero import LED
from gpiozero import Button

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


SCLK = 11
DIN = 10
DC = 23
RST = 24
CS = 8


# software spi
disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

led = LED(26)


button = Button(21)

disp.begin(contrast=60)


disp.clear()
disp.display()

image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

font = ImageFont.load_default()

draw = ImageDraw.Draw(image)


print("Press Ctrl-C to quit.")
while True:
        draw.rectangle((0,0,83,47), outline=255, fill=255)
        if button.is_pressed:
                draw.text((10,15), cpu(), font=font)
        else:
                draw.text((10,15), 'boia dell\'orso', font=font)
        disp.image(image)
        disp.display()
        led.on()
        time.sleep(0.4)
        led.off()
