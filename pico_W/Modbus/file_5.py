# Implementing an RTU

from umodbus.serial import Serial as ModbusRTUMaster
from machine import Pin

host = ModbusRTUMaster(
    pins=Pin(25,26)
)

# address of the target/client/slave device on the bus
slave_address = 10
coil_address = 123
coli_qty = 1 

coil_status = host.read_coils(
    slave_address = slave_address,
    starting_adddress = coil_address,
    coli_qty = coli_qty
)

print("Status of Coil {}: {}".format(coil_address, coil_status) )