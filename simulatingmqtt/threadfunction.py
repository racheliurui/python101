import time
from random import randrange
import sensorReading
import vars


#simulating sensor reading
def refresh_sensor1():
    while True:      
      sensorReading.sensor1_reading=str(randrange(10,20))


#simulating sensor reading
def refresh_sensor2():
    while True:
      sensorReading.sensor2_reading=str(randrange(10,20))
      
def killMain():    
    while True:
       i = input("Enter text (or Enter to quit): ")
       if not i:
          break
    print("Your input:", i)
    vars.quitMain=True
    print("While loop has exited")  