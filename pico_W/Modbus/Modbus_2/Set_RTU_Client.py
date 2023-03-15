# Import the modbus client class
from machine import Pin 
from umodbus.serial import ModbusRTU

# Set/map UART pins as a tuple for Comm.
rtu_pins = (Pin(4), Pin(5)) # TX, RX Respectively
uart_ID = 1 # since we are using pin 4/5, we map serial UART1 to GPIO4/5 hence 
            # the UART_ID = 1

slave_address = 1 # this is the address on the bus as client
baudrate = 115200 # the default is 9600 : most prefered

# print('Using Pins {} with UART ID {}'.format(rtu_pins, uart_ID)) # degugging

client = ModbusRTU(
    addr = slave_address,
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

# reset all registers back to their default value
register_definitions['COILS']['RESET_REGISTER_DATA_COIL']['on_set_cb'] = reset_data_regs
print('Setting-up Regs ...')
client.setup_registers(registers=register_definitions)
print('Register setup done')

print('Serving as RTU client on address {} at {} baud'.
      format(slave_address, baudrate))

while True:
    try:
        result = client.process()
    except KeyboardInterrupt:
        print('KeyboardInterrupt, stopping RTU client...')
        break
    except Exception as e:
        print('Exception during execution: {}'.format(e))

print("Finished providing/accepting data as client")