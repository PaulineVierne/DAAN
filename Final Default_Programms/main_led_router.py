import network
import time
import ubinascii
import micropython
import socket
import machine
import fading 
#import fading

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.ifconfig(('192.168.0.77','255.255.255.0','192.168.0.1','8.8.8.8'))
        sta_if.connect('Daan', '08774323')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    ap_if.active(False)


do_connect()

html = """<!DOCTYPE html>
<html lang="en">
<html>
<head><meta charset="utf-8">
<style>
body {background-color: white;}
h2   {color: black;}
p    {color: red;}
.button {
    background-color: grey; /* Green */
    border: none;
    color: white;  
    padding: 14px 25px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 25px;
}
.button2 {background-color: #50C88C;} /* Blue */
.button3 {background-color: black;} /* Red */ 
</style>   
<title>FIBEROPTIC LIGHT SHAWL</title> </head>
<h1>FIBEROPTIC LIGHT SHAWL<h1>
<form>
<button class="button button2" name="LED" value="ON0" type="submit">LED ON</button>
<button class="button" name="LED" value="OFF0" type="submit">LED OFF</button>
<br><br>
<button class="button button3"name="LED" value="Slowf" type="submit">Slowfade</button>
<button class="button button3"name="LED" value="Strobo" type="submit">Strobo</button>
<button class="button button3"name="LED" value="Blink" type="submit">Blink</button>
</form>
</html"""

#Setup PINS
#LED0 = machine.Pin(0, machine.Pin.OUT)
#LED2 = machine.Pin(2, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    LEDON0 = request.find('/?LED=ON0')
    LEDOFF0 = request.find('/?LED=OFF0')
    LEDON2 = request.find('/?LED=Slowf')
    LEDOFF2 = request.find('/?LED=Strobo')
    LEDBLINK = request.find('/?LED=Blink')
    #print("Data: " + str(LEDON0))
    #print("Data2: " + str(LEDOFF0))
    if LEDON0 == 6:
        fading.pwm3.freq(500)
        fading.pwm6.freq(500)
    	fading.pwm3.duty(700)
    	fading.pwm6.duty(700)
        #a = 1
        print('TURN LED0 ON')
    if LEDOFF0 == 6:
    	fading.pwm3.duty(0)
    	fading.pwm6.duty(0)
        #a = 2
        print('TURN LED0 OFF')
    if LEDON2 == 6:
        fading.pwm3.freq(500)
        fading.pwm6.freq(500)
        fading.controlfade_safe_both(40)
        #a = 3
        print('TURN Slofade ON')
    if LEDOFF2 == 6:
        #a = 4
        fading.pwm3.duty(700)
    	fading.pwm6.duty(700)
    	fading.pwm3.freq(13)
        fading.pwm6.freq(13)
        print('TURN Strobo ON')
    if  LEDBLINK == 6:
        #a = 4
        fading.pwm3.duty(700)
        fading.pwm6.duty(700)
        fading.pwm3.freq(1)
        fading.pwm6.freq(1)
        print('TURN Strobo ON')
    response = html
    conn.send(response)
    conn.close()