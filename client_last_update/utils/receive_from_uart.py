import serial
from utils.read_file import read_file
from utils.generate_formatted_string_from_json_string import generate_formatted_string_from_json_string
from utils.write_json_file import write_json_file




def receive_from_uart():
    ser = serial.Serial()
    ser.port = '/dev/ttyAMA0'
    ser.baudrate = 115200
    ser.timeout = 60
    ser.open()

    TXSize = 100
    RXSize = 100
    msgReceived = ''



    msgSent = read_file("utils/test.json")
    msgSent = generate_formatted_string_from_json_string(msgSent)
    print("msg sent:")
    print(msgSent)
    for i in range(len(msgSent), TXSize):
        msgSent += '!'

    ser.write(msgSent.encode())
    msgReceived = ser.read(RXSize)
    try:
        msgReceived.decode('utf-8')
        print(str(msgReceived)[2:])
        write_json_file("utils/aya.json", str(msgReceived)[2:])
    except (UnicodeDecodeError, AttributeError):
        print("error")
        pass
    if msgReceived == b'\r':
        return
    msgReceived = ''
