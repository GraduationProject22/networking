import files_locator
import os
import socket
import time

HEADER = 64
PORT = 5010
BUFFER_SIZE = 4096
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_file(filename):
    # the name of file we want to send, make sure it exists
    filename = str(filename)

    # get the file size
    filesize = os.path.getsize(filename)

    # send the filename and filesize
    client.send(f"{filename} {filesize}".encode())
    print(filename)

    # start sending the file
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in busy networks
            client.sendall(bytes_read)
        f.close()
    # # close the socket
    # client.close()


send_file("1.csv")
time.sleep(2.5)
send_file("2.csv")
# files = files_locator.files_locator(".", ".csv")
# for file in files:
#     send_file(file)
