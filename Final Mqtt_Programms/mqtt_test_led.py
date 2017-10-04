import network
import time
from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii
import machine
import micropython
import fading 

SERVER = "172.20.2.38"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"topic/test"
newmessage = False


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        #sta_if.ifconfig(('192.168.200.333','255.255.255.0','192.168.200.1','8.8.8.8'))
        #sta_if.ifconfig(('172.25.100.200 ','255.255.255.0','172.25.100.1 ','8.8.8.8'))
        #sta_if.connect('TGP', 'BRL4JHtv.Y21j6Uei-K9')
        sta_if.connect('Labs-Guest', 'L-G@UDK4GJ2015')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    ap_if.active(False)


def sub_cb(topic, msg):
    print((topic, msg))
    global newmessage
    
    if msg == b"on":
        fading.pwm3.freq(500)
        fading.pwm6.freq(500)
        fading.pwm3.duty(700)
        fading.pwm6.duty(700)
        #a = 1
        print('TURN LED0 ON')
    if msg == b"off":
        fading.pwm3.duty(0)
        fading.pwm6.duty(0)
        #a = 2
        print('TURN LED0 OFF')
    if msg == b"fade":
        fading.pwm3.freq(500)
        fading.pwm6.freq(500)
        fading.controlfade_safe_both(40)
        #a = 3
        print('TURN Slofade ON')
    if msg == b"blink_fast":
        #a = 4
        fading.pwm3.duty(700)
        fading.pwm6.duty(700)
        fading.pwm3.freq(13)
        fading.pwm6.freq(13)
        print('TURN Strobo ON')
    if msg == b"blink_slow":
        #a = 4
        fading.pwm3.duty(700)
        fading.pwm6.duty(700)
        fading.pwm3.freq(1)
        fading.pwm6.freq(1)
        print('TURN Strobo ON')
    if msg == b"testpattern":
        print('testpattern')
        fading.pwm3.freq(500)
        fading.pwm6.freq(500)
        fading.controlfade_safe_both(40)
        fading.pwm3.duty(700) #fast
        fading.pwm6.duty(700)
        fading.pwm3.freq(13)
        fading.pwm6.freq(13)
        time.sleep(10)        #
        fading.pwm3.duty(700)
        fading.pwm6.duty(700)
        fading.pwm3.freq(1)
        fading.pwm6.freq(1)
        time.sleep(10)
        fading.pwm3.freq(500)
        fading.pwm6.freq(500)
        fading.controlfade_safe_both(40)
        fading.pwm3.duty(700) #fast
        fading.pwm6.duty(700)
        fading.pwm3.freq(13)
        fading.pwm6.freq(13)
        time.sleep(10)        #
        fading.pwm3.duty(700)
        fading.pwm6.duty(700)
        fading.pwm3.freq(1)
        fading.pwm6.freq(1)
        time.sleep(10)
        #a = 4#

        #while True:
            # if newmessage == True:
            #     break
            # else:
            #     fading.pwm3.freq(500)
            #     fading.pwm6.freq(500)
            #     fading.controlfade_safe_both(40)



def out():
    for b in fading.lightarray:
        b.duty(0)

def main(server=SERVER):
    global newmessage
    out()
    do_connect()
    c = MQTTClient(CLIENT_ID, server)
    # Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))

    try:
        while 1:
            #micropython.mem_info()
            c.check_msg()
            #print (type(c.check_msg()))
            #a = c.check.msg() 
            #if a is not None:
            #    newmessage = True
            #elif c.check.msg() is None:
            #    newmessage = False
            time.sleep(1)

    finally:
		c.disconnect()

main()

