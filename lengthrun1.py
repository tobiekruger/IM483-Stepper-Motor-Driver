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
    GPIO.output(step_pin, 0)
 
def backwards(delay, steps):  
  GPIO.output(direction_pin, 0)
  for i in range(0, steps):
    GPIO.output(step_pin, 1)
    time.sleep(delay)
    GPIO.output(step_pin, 0)
 
 

delay = 15
steps = 4800
taken = 0

while taken < steps:
  start_time = time.time()
  forward(int(delay) / 10000.0, 2)
  elapsed_time = time.time() - start_time
  while elapsed_time < 1.5:
    elapsed_time = time.time() - start_time
    print 'getting to 1.5 seconds: %s' % elapsed_time
  
  
