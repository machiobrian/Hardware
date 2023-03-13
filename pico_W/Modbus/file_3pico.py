import machine
import umodbus
import ustruct

# Create a ModbusSlave instance with the appropriate serial port and baud rate
slave = modbus.ModbusSlave(machine.UART(0, baudrate=9600), mode=modbus.MODE_RTU)

# Define the addresses and values of the coils and holding registers
coil_values = [False, True, False, True, False, True, False, True]
holding_register_values = [1234, 5678]

# Define a function to handle Modbus requests
def handle_request(slave):
    request = slave.receive()
    if request.function_code == modbus.FUNCTION_READ_COILS:
        start_address = request.start_address
        num_coils = request.quantity
        coil_data = [0] * ((num_coils + 7) // 8)
        for i in range(num_coils):
            if coil_values[start_address + i]:
                coil_data[i // 8] |= 1 << (i % 8)
        response = modbus.ReadCoilsResponse(coil_data)
        slave.send(response)
    elif request.function_code == modbus.FUNCTION_READ_HOLDING_REGISTERS:
        start_address = request.start_address
        num_registers = request.quantity
        register_data = bytearray(num_registers * 2)
        for i in range(num_registers):
            value_bytes = ustruct.pack('>H', holding_register_values[start_address + i])
            register_data[i * 2:(i + 1) * 2] = value_bytes
        response = modbus.ReadHoldingRegistersResponse(register_data)
        slave.send(response)
    else:
        error = modbus.IllegalFunctionError(request.function_code)
        slave.send(error)

# Loop forever, handling Modbus requests
while True:
    handle_request(slave)
