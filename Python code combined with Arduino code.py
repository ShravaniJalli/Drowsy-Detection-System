import sys
import json
import serial
import time
import paho.mqtt.client as mqtt

#MQTT parameters
host='ptfjhr.messaging.internetofthings.ibmcloud.com'
clientid='d:ptfjhr:Eyeblinkingsensor:Arduino'
authMethod='use-token-auth'
token='4z0pZBi86mmA30yqkx'

topic='iot-2/evt/python4/fmt/json'
IRsensor=13

client=mqtt.Client(clientid)
client.username_pw_set(authMethod,token)
client.connect(host,1883,60)

arduino=serial.Serial('COM4', 9600)
print("You have a new msg from Arduino")

try:
    while 1:
        response=arduino.readline()
        print("Message Published")
        print(response)
except KeyboardInterrupt:
    arduino.close()
except IOError:
    print("Error")

client.loop()
client.disconnect()

    
