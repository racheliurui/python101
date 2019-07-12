import json
import time
import sensorReading
#simulating publish
#With our setup, it was possible to send on average 8 to 9 messages per second with qos=2, that means acknowledged messages. 

def publish_readings():
    while True:
      data = {}
      data['sensor1_reading'] = sensorReading.sensor1_reading
      data['sensor2_reading'] = sensorReading.sensor2_reading
      print("sensor reading published as  " + json.dumps(data) )  
      time.sleep(0.1)