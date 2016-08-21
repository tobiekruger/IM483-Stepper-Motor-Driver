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
 
 
while True:
  delay = raw_input("Delay between steps (milliseconds)?")
  steps = raw_input("How many steps forward? ")
  
  start_time = time.time()
  forward(int(delay) / 10000.0, int(steps))
  elapsed_time = time.time() - start_time
  print 'Total time: %s' % elapsed_time
  steps = raw_input("How many steps backwards? ")
  backwards(int(delay) / 10000.0, int(steps))
