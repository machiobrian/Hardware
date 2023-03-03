import network
import time
from secrets import *

def do_connect(ssid=secrets['ssid'], psk=secrets['password']):
    # station/client: connects to upstream wifi access points
    wlan = network.WLAN(network.STA_IF) 
    wlan.active(True)
    wlan.connect(ssid, psk)
    
    # wait for connnection to fail
    wait = 10
    while wait > 0:
        if wlan.status() < 0 or wlan.status() >=3 :
            break
        wait -= 1
        print('waiting for connection ... ')
        time.sleep(1)
        
    # this is how we handle connection error
    if wlan.status() != 3:
        raise RuntimeError('wifi connection failed ... ')
    else:
        print('connected')
        ip = wlan.ifconfig()[0]
        print('network config: ', ip)
        return ip