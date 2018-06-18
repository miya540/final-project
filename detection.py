import RPi.GPIO as gpio
import time

DISPLAY = [0x06,0x5B,0x4F,0x66,0x6D]

gpio.setmode(gpio.BOARD)
gpio.setup(26,gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(11,gpio.OUT)
gpio.setup(7,gpio.OUT)

gpio.setup(33,gpio.OUT)
gpio.setup(31,gpio.OUT)
gpio.setup(36,gpio.OUT)
gpio.setup(38,gpio.OUT)
gpio.setup(40,gpio.OUT)
gpio.setup(35,gpio.OUT)
gpio.setup(37,gpio.OUT)
gpio.setup(32,gpio.OUT) 

gpio.output(7, True)

def action(channel):
    gpio.output(7, False)
    print ("Motion detected")
    for i in range(5):
        gpio.output(11, True)
        pin = DISPLAY[i]        # assigning value to 'pin' for each digit
        PORT(pin);                  # showing each digit on display 
        time.sleep(0.5)
        gpio.output(11, False)
        time.sleep(0.2)
    gpio.output(7, True)

def PORT(pin):                    # assigning GPIO logic by taking 'pin' value
    if(pin&0x01 == 0x01):
        gpio.output(33,1)            # if  bit0 of 8bit 'pin' is true, pull PIN33 high
    else:
        gpio.output(33,0)            # if  bit0 of 8bit 'pin' is false, pull PIN33 low
    if(pin&0x02 == 0x02):
        gpio.output(31,1)             # if  bit1 of 8bit 'pin' is true, pull PIN31 high
    else:
        gpio.output(31,0)            #if  bit1 of 8bit 'pin' is false, pull PIN31 low
    if(pin&0x04 == 0x04):
        gpio.output(36,1)           
    else:
        gpio.output(36,0)
    if(pin&0x08 == 0x08):
        gpio.output(38,1)
    else:
        gpio.output(38,0)   
    if(pin&0x10 == 0x10):
        gpio.output(40,1)
    else:
        gpio.output(40,0)
    if(pin&0x20 == 0x20):
        gpio.output(35,1)
    else:
        gpio.output(35,0)
    if(pin&0x40 == 0x40):
        gpio.output(37,1)
    else:
        gpio.output(37,0)
    if(pin&0x80 == 0x80):
        gpio.output(32,1)            # if  bit7 of 8bit 'pin' is true, pull PIN32 high
    else:
        gpio.output(32,0)            # if  bit7 of 8bit 'pin' is false, pull PIN322 low
        
 
try:
    gpio.add_event_detect(26, gpio.RISING, callback=action, bouncetime=200)
    while True:
        time.sleep(1)
except:
    gpio.cleanup()
