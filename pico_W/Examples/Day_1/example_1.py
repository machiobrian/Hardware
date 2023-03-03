# connect to the wifi: read on-board temp, on-board LED

import network
import socket
 
from time import sleep
from picozero import pico_temp_sensor, pico_led

import machine

ssid = "_braen"
password = "Callmebr@3n"

# build a function to connect to the WLAN

def connect():
    # connect to LAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # function to loop a request until a handshake is established
    
    while wlan.isconnected() == False:
        print("Waiting for connection ... ")
        sleep(1) # hopefully its microseconds : apparently thi is seconds
        # sleep_ms(), sleep_us()
        
    print(wlan.ifconfig()) # prints the entire sets of configs
    
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}') # prints only one ip: the one used.
    
try:
    connect()
except KeyboardInterrupt:
    machine.reset()
    
# a function to open a socket    
def open_socket(ip):
    # open a socket
    address = (ip, 80)
    # create a socket: and have it listen to port 80
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    
try:
    ip = connect()
    open_socket(ip)
except KeyboardInterrupt:
    machine.reset()
    



































