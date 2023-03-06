import machine 
import utime
import ustruct
import sys 

##################################################################################

# set up some constants

# neccessary registers

REG_DEVID = 0x00
REG_POWER_CTL = 0x2D
REG_DATAX0 = 0x32

DEVID = 0xE5
SENSITIVITY_2G = 1.0/256 #g/LSB
EARTH_GRAVITY = 9.80665 # earth's gravity in m/s^2

##################################################################################

# Settings : Assing Chip Select (SS) pin and start at HIGH(1)
cs = machine.Pin(17, machine.Pin.OUT)

# construct an SPI object
spi = machine.SPI(
    0, # id SPI0
    
    polarity=1, # state of the clk signal when idle
    phase=1, # how data is sampled: rising/falling edge

    bits=8,
    firstbit=machine.SPI.MSB,

    sck=machine.Pin(18), # system clock : SPI0 SCK
    mosi=machine.Pin(19), # master out slave in: SPI0 TX
    miso=machine.Pin(16) # master in slave out : SPI0 RX
)

##################################################################################

# Functions

def reg_write(spi, sc, reg, data):
    """
    write `1 byte` to the specified register
    """
    # construct a message (set ~W bit low, MB bit low) - MB - Multiple Byte
    msg = bytearray()
    msg.append(0x00 | reg)
    msg.append(data)

    # send out SPI message
    cs.value(0) # get/sets the logic level of the pin.
    spi.write(msg) # write the number of bytes contained in .buf
    cs.value(1)

def reg_read(spi, sc, reg, nbytes=1):
    """
    Read bytes from specified register. If nbytes>1, read from consecutive regs
    """
    # Determine if multiple byte but should be set
    if nbytes < 1:
        return bytearray()
    elif nbytes == 1:
        mb = 0
    else:
        mb =1

    # Construct message (set ~W bit high)
    msg = bytearray()
    msg.append(0x80 | (mb<<6) | reg)

    # send out SPI message and read
    cs.value(0)
    spi.write(msg)
    data = spi.read(nbytes)
    cs.value(1)

    return data

##################################################################################

# Main

# start the CS pin High
cs.value(1)

# A workaround that performs throw-away read to make SCK idle HIGH
reg_read(spi, cs, reg=REG_DEVID)

# Read the device ID to make sure we are communicating with ADXL343
data = reg_read(spi, cs, REG_DEVID)
if (data != bytearray((DEVID,))):
    print("Error: Could not communicate with ADxL343")
    sys.exit()

# Read the Power control register
data = reg_read(spi, cs, REG_POWER_CTL)
print(data)

# tell the accel to start taking measurements by setting measre bit to high

data = int.from_bytes(data, "big") | (1 << 3) # return integer represented by 
                                              # the given array of bytes

# Test : Read the Power Control Register "again" to ensure Measure Bit was set.
data = reg_read(spi, cs, REG_POWER_CTL) 

# wait before taking measurements
utime.sleep(2.0)

# Run continuously.
while True:
    # Read X,Y,Z values from registers (16 Bit)
    data = reg_read(spi, cs, reg=REG_DATAX0, nbytes=6)

    # convert 2 bytes into 16-bit integer | signed integer
    acc_x = ustruct.unpack_from("<h", data, 0)[0]
    acc_y = ustruct.unpack_from("<h", data, 2)[0]
    acc_z = ustruct.unpack_from("<h", data, 4)[0]

    # convert measuremets to m/s^2
    print("X:", "{:.2f}".format(acc_x), \
          "| Y:", "{:.2f}".format(acc_y), \
          "| Z:", "{:.2f}".format(acc_z))
    
    utime.sleep(0.1)