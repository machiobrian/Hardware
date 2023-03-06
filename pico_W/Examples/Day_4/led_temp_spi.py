"""
Define the Chip Select Pins and Initialize the SPI bus.
Confgure temp sensor by: Sending a config command over SPI
"""

import machine
import utime
import ustruct
import sys 


# intialize a temperature _sensor register
REG_TEMP = 0x0B