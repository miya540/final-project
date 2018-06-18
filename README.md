# final－project_PIR sensor with LED & sevensegment

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
- Pysical PIN6 to PIR-OUT (signal out)
- Pysical PIN26 to PIR-GND (ground power)
- Pysical PIN2 to PIR-VCC (3-5VDC voltage power)

### Wiring up sevensegment
![image](https://github.com/miya540/final-project/blob/master/7%20segment.jpg)
