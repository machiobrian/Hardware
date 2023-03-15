# import serial
from umodbus.serial import Serial
import struct

# Modbus function codes
READ_COILS = 0x01
READ_DISCRETE_INPUTS = 0x02
READ_HOLDING_REGISTERS = 0x03
READ_INPUT_REGISTERS = 0x04
WRITE_SINGLE_COIL = 0x05
WRITE_SINGLE_REGISTER = 0x06
WRITE_MULTIPLE_COILS = 0x0F
WRITE_MULTIPLE_REGISTERS = 0x10

class ModbusClient:
    def __init__(self, port, baudrate=9600):
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=1)

    def send_packet(self, address, function_code, data):
        packet = struct.pack('>BB', address, function_code) + data
        crc = self.calculate_crc(packet)
        packet += struct.pack('<H', crc)
        self.ser.write(packet)

    def receive_packet(self):
        # Read header
        header = self.ser.read(2)
        if len(header) != 2:
            raise Exception('Incomplete packet')
        address, function_code = struct.unpack('>BB', header)

        # Read data
        if function_code in (READ_COILS, READ_DISCRETE_INPUTS, READ_HOLDING_REGISTERS, READ_INPUT_REGISTERS):
            # Read length field
            length = struct.unpack('>H', self.ser.read(2))[0]
            data = self.ser.read(length)
        elif function_code in (WRITE_SINGLE_COIL, WRITE_SINGLE_REGISTER, WRITE_MULTIPLE_COILS, WRITE_MULTIPLE_REGISTERS):
            # Read address and value fields
            address, value = struct.unpack('>HH', self.ser.read(4))
            data = (address, value)
        else:
            raise Exception('Unknown function code')

        # Read CRC
        crc = struct.unpack('<H', self.ser.read(2))[0]
        if crc != self.calculate_crc(header + data):
            raise Exception('Invalid CRC')

        return (address, function_code, data)

    def calculate_crc(self, data):
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        return crc

    def read_coils(self, address, start_address, num_coils):
        data = struct.pack('>HH', start_address, num_coils)
        self.send_packet(address, READ_COILS, data)
        response = self.receive_packet()
        _, function_code, data = response
        if function_code != READ_COILS:
            raise Exception('Unexpected function code')
        return list(map(bool, data))

    def read_holding_registers(self, address, start_address, num_registers):
        data = struct.pack('>HH', start_address, num_registers)
        self.send_packet(address, READ_HOLDING_REGISTERS, data)
        response = self.receive_packet()
        _, function_code, data = response
        if function_code != READ_HOLDING_REGISTERS:
            raise Exception('Unexpected function code')
        return
