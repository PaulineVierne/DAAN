# DAAN
DAAN Prototype Sourcecodes

This is the source code repository for three prototypes developed at the Design Research Lab in the DAAN Project between 2016-2017. The prototyps consits of diffrent electric circuits build arround a Node MCU Mircocontroller. A detailed Documentation of the electric circuit and the building elements can be found in the attached PDFs. 

In "Default mode" the controllers are integrated in an WIFI Network generated by an TPLINK. A HTML interface for every Controller can be found at:

Lightshawl:             192.168.0.77  
Thermohapticshawl:      192.168.0.88 
Thermocromicshawl:      192.168.0.88 


Default Use:

1.Turn on the TPLINK
2.Turn on the Shawl
3.Connect to the TPLink Network named "Daan" (Password should be known by you)
4.Type the IP Adress in your Browserbar (This should work independent of the device) 


MQTT:

The controllers can also be used as MQTT SUBSCRIBERS. This is usefull when trying to integrate them in a bigger Setup. In this Setup the controller act as a MQTT SUBSCRIBER, meaning it needs a mqtt broker. The Setup can be tested by installing mosquitto locally. On Mac this can be done with homebrew (if you don't have homebrew installed: https://brew.sh/index_de.html) 

brew install mosquitto

A Command to the Shawl can be send:

mosquitto_pub -t topic/test -m "Blink"

Find a PDF in the repository with the all the functions of the keyword.


Standalone Use:

The controllers can also be used as Standalone. We experienced connect troubles while trying these.
To use them in Standalone Mode upload the provided Standalone Code.


How to upload code:

A detailed tutorial can be found here:
https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html

A active micropython shell over usb:
picocom /dev/ttyUSB0 -b115200
 
The main file tranfer works through Webrpl and websockets:
https://github.com/micropython/webrepl

To tranfer a file clone or download the https://github.com/micropython/webrepl to your computer. Navigate to the folder. The Syntax of the command looks like:  

python webrepl_cli.py THE_NAME_OF_YOU_SCIPT_TOUPLOAD.py THE_IP_ADRESS_OF_YOUR_CONTROLLER:THE_NAME_OF_THE_SCRIPT.py

Example:

python webrepl_cli.py script.py 192.168.0.77:main.py


Copyright (c) 2017 Design Research Lab 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


