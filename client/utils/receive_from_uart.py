import serial
from utils.read_file import read_file
from utils.generate_formatted_string_from_json_string import generate_formatted_string_from_json_string
from utils.write_json_file import write_json_file


def receive_from_uart():
    ser = serial.Serial()
    ser.port = '/dev/ttyAMA0'
    ser.baudrate = 115200
    ser.timeout = 5
    ser.open()

    TXSize = 50
    RXSize = 200
    msgReceived = ''
    toBeConverted = ''
    indexStart = 0
    indexEnd = 0

    msgSent = read_file("test.json")
    msgSent = generate_formatted_string_from_json_string(msgSent)
    print("msg sent:")
    print(msgSent)
    for i in range(len(msgSent), TXSize):
        msgSent += '.'

    ser.write(msgSent.encode())
    msgReceived = ser.read(RXSize)
    try:
        msgReceived.decode('utf-8')
        for i in range(0, RXSize):
            if(msgReceived[i] == 61):
                indexStart = i - 1
                break
        for i in range(indexStart, RXSize):
            if(msgReceived[i] == 46):
                indexEnd = i
                break
        toBeConverted = msgReceived[indexStart:indexEnd]

        print(toBeConverted)
        print(len(toBeConverted))
# error		msgReceived = msgReceived.translate({ord('?'): None})
        #print (msgReceived)
        write_json_file("received-test.json", str(toBeConverted)[2:])
    except (UnicodeDecodeError, AttributeError):
        print("error")
        pass
    if msgReceived == b'\r':
        return
    msgReceived = ''
