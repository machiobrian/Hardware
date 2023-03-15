# Import the modbus client class
from machine import Pin 
from umodbus.serial import ModbusRTU

# Set/map UART pins as a tuple for Comm.
rtu_pins = (Pin(4), Pin(5)) # TX, RX Respectively
uart_ID = 1 # since we are using pin 4/5, we map serial UART1 to GPIO4/5 hence 
            # the UART_ID = 1

slave_address = 10 # this is the address on the bus as client
baudrate = 115200 # the default is 9600

# print('Using Pins {} with UART ID {}'.format(rtu_pins, uart_ID)) # degugging

client = ModbusRTU(
    address = slave_address,
    pins = rtu_pins,
    baudrate = baudrate,
    uart_id = uart_ID
)
# Perfome a register reset
def reset_data_regs(reg_type, address, value):
    global client
    global register_definitions

    print('Resetting Reg to Default Vaues ...')
    client.setup_registers(
        registers=register_definitions)
    print("Default Values Restored")

# Common Slave Register Setups : Starting Points

register_definitions = {
    "COILS":{
        "RESET_REGISTER_DATA_COIL": {
            "register": 42,
            "len": 1,
            "val": 0
        },
        "EXAMPLE_COIL": {
            "register": 123,
            "len": 1,
            "val": 1
        }
    },
    "HREGS": { # Holding Registers
        "EXAMPLE_HREG": {
            "register": 93,
            "len": 1,
            "val": 19
        }
    },
    "ISTS": { # Input Status
        "EXAMPLE_ISTS": {
            "register": 67,
            "len": 1,
            "val": 0
        }
    },
    "IREGS": { # Input Registers
        "EXAMPLE_IREG": {
            "register": 10,
            "len": 1,
            "val": 60001
        }
    }
}

