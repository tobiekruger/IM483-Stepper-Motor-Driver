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
steps = 6400
taken = 0

button_time = time.time()

while taken < steps:
  start_time = time.time()
  forward(int(delay) / 10000.0, 1)
  taken = taken + 1
  elapsed_time = time.time() - start_time
  button_elapsed = time.time() - button_time
  print 'total time: %s' % button_elapsed
  print 'total steps: %s' % taken
  while elapsed_time < 1:
    elapsed_time = time.time() - start_time    
  
  
