READ_COILS = 0x01
READ_HOLDING_REGISTERS = 0x03

import serial
from serial import Serial
import struct

class ModbusClient: # handles communication with the device over the serial port
                    # the class has methods to send and receive Modbus packets, also
                    # higher methods to read and write coils and holding registers
    def __init__(self, port, baudrate):
        self.serial_port = serial.Serial(port=port, baudrate=baudrate)

    def send_packet(self, address, function_code, data):
        packet = struct.pack(">BB" + str(len(data)) + "s", address, function_code, data)
        crc = self.calculate_crc(packet)
        packet_with_crc = packet + crc
        self.serial_port.write(packet_with_crc)

    def receive_packet(self):
        response = self.serial_port.read(5)
        byte_count = response[2]
        data = self.serial_port.read(byte_count+2)
        packet = response + data
        crc = self.calculate_crc(packet[:-2])
        if crc != packet[-2:]:
            raise Exception("Invalid CRC")
        return packet

    def calculate_crc(self, data):
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for i in range(8):
                if crc & 0x0001:
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        crc_bytes = struct.pack("<H", crc)
        return crc_bytes

    # construct Modbus packets with appropriate function codes and data
    def read_coils(self, address, start_address, num_coils):
        data = struct.pack(">HH", start_address, num_coils)
        self.send_packet(address, READ_COILS, data)
        packet = self.receive_packet()
        byte_count = packet[2]
        coils = packet[3:3+byte_count]
        return coils

    def read_holding_registers(self, address, start_address, num_registers):
        data = struct.pack(">HH", start_address, num_registers)
        self.send_packet(address, READ_HOLDING_REGISTERS, data)
        packet = self.receive_packet()
        byte_count = packet[2]
        registers = packet[3:3+byte_count]
        return registers

# create an instance of the modbus client class with appropriate serial port and baudrate
client = ModbusClient('/dev/ttyACM0', 9600)

# Call methods to read and write data
coils = client.read_coils(1, 0, 8)
print("Coils:", coils)
registers = client.read_holding_registers(1, 0, 2)
print("Registers:", registers)