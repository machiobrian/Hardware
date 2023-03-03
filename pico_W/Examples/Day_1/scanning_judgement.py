import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("_braen","Callmebr@3n")

# wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print("waiting for connection ... ")
    time.sleep(1)
    
# handle connection error
if wlan.status() != 3: # status returns the current status of the wireless connection
    raise RuntimeError('wifi connection failed ... ')
else:
    print('connected')
    print('IP: ', wlan.ifconfig()[0])
    # ifconfig() returns : IP addresses, subnet masks, gateways and DNS servers.
    # the method returns a 4 tuple containing the above information