import network
import time
import ubinascii
import micropython
import socket
import machine
# letzte field more power / 
p2 = machine.Pin(4)
pwm2 = machine.PWM(p2)

p5 = machine.Pin(14)
pwm5 = machine.PWM(p5)

p6 = machine.Pin(12)
pwm6 = machine.PWM(p6)

p8 = machine.Pin(15)
pwm8 = machine.PWM(p8)

heatarray = [pwm8,pwm6,pwm5,pwm2]
beginningvalue = 200
beginningvalue_small = 0

#small wiederstand to big indication which buttons 

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
<title>Thermochromic heat shawl</title> </head>
<h2>Thermochromic heat shawl</h2>
<form>
<button class="button button2" name="LED" value="ON0" type="submit">Heating Full</button>
<button class="button button3" name="LED" value="ONSMALL" type="submit">Heating Soft</button><br><br>
<button class="button button3" name="LED" value="ONFIRST" type="submit">Heating Group1</button>
<button class="button button3" name="LED" value="ONSECOND" type="submit">Heating Group2</button>
<button class="button" name="LED" value="OFF0" type="submit">Heating off</button><br><br>
</form>
</html>
"""
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.ifconfig(('192.168.0.99','255.255.255.0','192.168.0.1','8.8.8.8'))
        sta_if.connect('Daan', '08774323')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    ap_if.active(False)


do_connect()


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
    LEDONSMALL= request.find('/?LED=ONSMALL')
    LEDONFIRST = request.find('/?LED=ONFIRST')
    LEDONSECOND = request.find('/?LED=ONSECOND')
    #print("Data: " + str(LEDON0))
    #print("Data2: " + str(LEDOFF0))
    if LEDON0 == 6:
        #for i in range(0,4):
        #    beginningvalue = beginningvalue +100
        #    heatarray[i].duty(beginningvalue)
        heatarray[0].duty(beginningvalue+100)
        heatarray[1].duty(beginningvalue+150)
        heatarray[2].duty(beginningvalue+100)
        heatarray[3].duty(beginningvalue+200)
        print('TURN LED0 ON')
    if LEDOFF0 == 6:
    	for i in heatarray:
    		i.duty(0)
        beginningvalue = 200
        print('TURN LED0 OFF')
    if LEDONSMALL == 6:
        heatarray[0].duty(beginningvalue_small+100)
        heatarray[1].duty(beginningvalue_small+150)
        heatarray[2].duty(beginningvalue_small+100)
        heatarray[3].duty(beginningvalue_small+200)
        print('TURN LED0 SMALL')
    if LEDONFIRST ==6:
        heatarray[0].duty(20)
        heatarray[1].duty(beginningvalue+150)
        heatarray[2].duty(beginningvalue+100)
        heatarray[3].duty(20)
    if LEDONSECOND ==6:
        heatarray[0].duty(beginningvalue+100)
        heatarray[1].duty(20)
        heatarray[2].duty(20)
        heatarray[3].duty(beginningvalue+200)
    response = html
    conn.send(response)
    conn.close()

