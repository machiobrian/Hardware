from umodbus.serial import ModbusRTU
from machine import Pin

# RTU Client/Slave Setup
rtu_pins = (
    Pin(0), #TX
    Pin(1)  #RX
)
uart_id = 0 # check official documentation

rtu_pins = (
    Pin(4), #TX
    Pin(5)  #RX
)
uart_id = 1

slave_address = 10 # address on bus as client

client = ModbusRTU(
    addr = slave_address, #  the address on the bus
    pins = rtu_pins,      #  TX, RX
    baudrate = 9600,
    data_bits = 8,
    stop_bits = 1,
    parity = None,
    ctrl_pin = 12,
    uart_id = uart_id
)

register_definitions = {
    "COILS":{
        "EXAMPLE_COIL":{
            "register":123,
            "len":1,
            "val":13
        }
    },
    "HREGS": {
        "EXAMPLE_HREG": {
            "register": 93,
            "len": 1,
            "val": 19
        }
    },
    "ISTS": {
        "EXAMPLE_ISTS": {
            "register": 67,
            "len": 1,
            "val": 0
        }
    },
    "IREGS": {
        "EXAMPLE_IREG": {
            "register": 10,
            "len": 1,
            "val": 60001
        }
    }
}

client.setup_registers(
    registers = register_definitions
)
while True:
    try:
        result = client.process()
        print(result)
    except KeyboardInterrupt():
        print("Stopping RTU Client...")
        break
    except Exception as e:
        print('Exception during execution: {}'.format(e))