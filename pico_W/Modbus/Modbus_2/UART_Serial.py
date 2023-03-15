# Serial Bus

"""
There are two UARTs : UART0/1. 
They can be mapped to GPIO:0/1, 12/13 and 16/17 -> UART0
                      GPIO:4/5, 8/9             -> UART1
"""
from machine import UART, Pin 
uart1 = UART(
    1, # ID
    baudrate = 9600,
    tx = Pin(8),
    rx = Pin(9)
)
uart1.write('hello') # writing 8 bytes
uart1.read(5) # read upto 8 bytes
