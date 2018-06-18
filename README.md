# final project_PIR sensor with LED & sevensegment

The green LED light up when motion is not detected.
When motion is detected, the green LED will turn off, the red LED will light up five times, and the sevensegment will read five seconds.

## Step 1 : The hardware
![image](https://github.com/miya540/final-project/blob/master/IMG_5033.JPG)

### What You Need:
- Raspberry Pi 3
- PIR sensor
- Breadboard
- 11x M-to-F jumper wires
- 3x F-to-F jumper wires
- 1x Red LED
- 1x Green LED
- 2x 220 Ω carbon film resistor
- 1x Cathode 7 segment display

### Wiring up PIR Sensor & Pi
Your PIR sensor should have 3-pin connection. 
Wire up to PIR Sensor & Pi as following:
![image](https://github.com/miya540/final-project/blob/master/S__12476421.jpg)
- Physical Pin6 to PIR-OUT (signal out)
- Physical Pin26 to PIR-GND (ground power)
- Physical Pin2 to PIR-VCC (3-5VDC voltage power)

### Wiring up sevensegment & Pi

![image](https://github.com/miya540/final-project/blob/master/7%20segment.jpg)
Sevensegment to any point on the bread board
- Physical Pin31 to b
- Physical Pin33 to a
- Physical Pin39 to com 
- Physical Pin35 to f 
- Physical Pin37 to g 
- Physical Pin36 to c 
- Physical Pin38 to d
- Physical Pin40 to e

### Wiring up LED & Pi & Breadboard
![image](https://github.com/miya540/final-project/blob/master/LED.jpg)
- Physical Pin7 to the positive end of the green LED(anode), and the cathode to the resistor
- Physical Pin11 to the positive end of the red LED(anode), and the cathode to the resistor
- Physical Pin9 & two resistor to the negative in breadboard


## Step 2 : The software
### The code 
The motion sensor is designed to send a web based alarm and light up the red light, when it detects motion.

### Breaking up the code
#### Line by line explanation of what the code does:
- **gpio** to access the GPIO (general purpose input output)pins on the Raspberry Pi. This library lets handles the interfacing with the pins.
- **time** to control Flashing intervel.
 ```python
import RPi.GPIO as gpio
import time
```

Setting the number 1-5 to count times
 ```python
DISPLAY = [0x06,0x5B,0x4F,0x66,0x6D]
 ```
 
- **setmode** : set up Pin numbering
Set Pin 26(PIR sensor) as input, and tell the Pi to pull up a Resistor on PIN26. Now the PI will look for low voltage on PIN26.
Then set Pin 11(Red LED) & 7(Green LED) as output.
 ```python
gpio.setmode(gpio.BOARD)
gpio.setup(26,gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(11,gpio.OUT)
gpio.setup(7,gpio.OUT)
 ```

Set Pin 33, 31, 36, 38, 40, 35, 37, 32(sevensegment as output).
 ```python
gpio.setup(33,gpio.OUT)
gpio.setup(31,gpio.OUT)
gpio.setup(36,gpio.OUT)
gpio.setup(38,gpio.OUT)
gpio.setup(40,gpio.OUT)
gpio.setup(35,gpio.OUT)
gpio.setup(37,gpio.OUT)
gpio.setup(32,gpio.OUT)
 ```

Let green LED light up as usual. 
 ```python
gpio.output(7, True)
  ```

When motion is detected, the green LED turn off, and print "Motion detected".
Set range 1 to 5, and the red LED will light up five times.
- **pin = DISPLAY[i]** assign value to 'pin' for each digit.
- **PORT(pin)** show each digit on display.
Then the green light will light up again to show motion is not detected now.
 ```python
def action(channel):
    gpio.output(7, False)
    print ("Motion detected")
    for i in range(5):
        gpio.output(11, True)
        pin = DISPLAY[i]       
        PORT(pin);                 
        time.sleep(0.5)
        gpio.output(11, False)
        time.sleep(0.2)
    gpio.output(7, True)
 ```

Assign GPIO logic by taking 'pin' value, and judge "pin" is true or false to pull Pin high or low.
 ```python 
 def PORT(pin):                    
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
```

Set detect event to call action.
 ```python
try:
    gpio.add_event_detect(26, gpio.RISING, callback=action, bouncetime=200)
    while True:
        time.sleep(1)
```

**Exiting your program cleanly**

RPi.GPIO provides a built-in function GPIO.cleanup() to clean up all the ports you’ve used. It only affects any ports you have set in the current program. It resets any ports you have used in this program back to input mode. 

 ```python
except:
    gpio.cleanup()
```
