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
- sevensegment to any point on the bread board
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
