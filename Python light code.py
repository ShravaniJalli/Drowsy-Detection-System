import time
import random
import sys
import ibmiotf.application
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "4aa10n" # repalce it with organization ID
deviceType = "Lights" #replace it with device type
deviceId = "simple" #repalce with device id
authMethod = "token"
authToken = "OkJJz_g69pXCG5)@Ib"#repalce with token

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)        
        if cmd.data['command']=='lighton':
                print("LIGHT ON")
        elif cmd.data['command'] == 'lightoff':
            print("LIGHT OFF")
                
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
        B=random.random();
        D=random.random();
        #Send Blinking timing & distance  to IBM Watson
        data = { 'Blinking_time' : B, 'Distance': D }
        #print data
        def myOnPublishCallback():
            print ("Published Blinking_time = %s seconds" % (B*100), "distance= %s %% cm" %( D*100), "to IBM Watson")

        success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
