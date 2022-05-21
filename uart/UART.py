import serial
from read_file import read_file
from format_json_string import format_json_string
from write_json_file import write_json_file


ser = serial.Serial()
ser.port = '/dev/ttyAMA0'
ser.baudrate = 115200
ser.timeout = 60
ser.open()

TXSize = 50
RXSize = 50
msgReceived = ''

#msgSent = input("Write: ")
msgSent = read_file("test.json")
msgSent = format_json_string(msgSent)
for i in range(len(msgSent), TXSize):
    msgSent += '.'
ser.write(msgSent.encode())
while True:
    msgReceived = ser.read(RXSize)
    try:
        msgReceived.decode()
        print(msgReceived)
        write_json_file("received-test.json", msgReceived)
    except (UnicodeDecodeError, AttributeError):
        print("error")
        pass
    if msgReceived == b'\r':

        break
    msgReceived = ''
