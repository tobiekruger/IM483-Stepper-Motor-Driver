# GPIO 17 - step clock
# GPIO 27 - direction
# GPIO 18 - enable

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
 
enable_pin = 18
step_pin = 17
direction_pin = 27

 
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(direction_pin, GPIO.OUT)
 
GPIO.output(enable_pin, 1)
 
def forward(delay, steps):  
  GPIO.output(direction_pin, 1)
  for i in range(0, steps):
    GPIO.output(step_pin, 1)
    time.sleep(delay)
 
def backwards(delay, steps):  
  GPIO.output(direction_pin, 0)
  for i in range(0, steps):
    GPIO.output(step_pin, 1)
    time.sleep(delay)
 
 
while True:
  delay = raw_input("Delay between steps (milliseconds)?")
  steps = raw_input("How many steps forward? ")
  forward(int(delay) / 1000.0, int(steps))
  steps = raw_input("How many steps backwards? ")
  backwards(int(delay) / 1000.0, int(steps))
