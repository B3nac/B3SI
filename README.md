# B3SI
Raspberry Pi Sensor Interface using Pyserial and Arduino

B3SI is a sensor interface for my space balloon/robot projects. It reads all serial output from Arduino and logs it with Python through a usb connection. My goal is to create a solid efficient sensor interface for collecting data from the atmosphere. 

##So far in v0.0.4:##

1. Reads and logs CPU temps.

2. Logs atmosphere temps and humidity. #Needs arduino connected via usb and Pyserial installed on Raspberry Pi.

3. Takes pictures through a webcam. *Note*: You need a webcam connected via usb.

4. Sorts unique strings that are logged. #No logging function yet.

Might get rid of uniq_sort. Haven't found a use for sorting uniques yet. I think I might want all data collected.
