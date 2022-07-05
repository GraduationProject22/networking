import json
import serial
from os import listdir
from utils.read_file import read_file
from utils.generate_formatted_string_from_json_string import generate_formatted_string_from_json_string
from utils.write_json_file import write_json_file
from utils.get_ip_address import get_ip_address


def receive_from_uart():
    ser = serial.Serial()
    ser.port = '/dev/ttyAMA0'
    ser.baudrate = 115200
    ser.timeout = 5
    ser.open()

    TXSize = 100
    RXSize = 100
    msgReceived = ''

    if (len(listdir("./received_files")) > 0):
        msgSent = read_file(listdir("./received_files")[0])
        json_obj = json.loads(msgSent)
        json_obj.pop("W")
        msgSent = generate_formatted_string_from_json_string(json_obj)
        print("msg sent:")
        print(msgSent)
        for i in range(len(msgSent), TXSize):
            msgSent += '!'
        ser.write(msgSent.encode())

    msgReceived = ser.read(RXSize)
    try:
        msgReceived.decode('utf-8')
        if(len(str(msgReceived)) > 3):
            print(str(msgReceived)[2:])
            write_json_file("./files_to_be_sent/" + get_ip_address() + ".json",
                            str(msgReceived)[2:])
    except (UnicodeDecodeError, AttributeError):
        print("error")
        pass
    if msgReceived == b'\r':
        return
    msgReceived = ''
