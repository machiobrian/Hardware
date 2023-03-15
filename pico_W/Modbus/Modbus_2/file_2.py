from umodbus.serial import ModbusRTU
from machine import Pin

rtu_pins = (
    Pin(4), #TX
    Pin(5)  #RX
)

slave_address = 10
coil_address = 123
coil_qty = 1

host = ModbusRTU(
    addr = slave_address,
    pins = rtu_pins
)

coil_status = host.read_coils(
    slave_addr=slave_address,
    starting_addr=coil_address,
    coil_qty=coil_qty)
print('Status of coil {}: {}'.format(coil_address, coil_status))