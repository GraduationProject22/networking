import os
import socket
from buffer import Buffer
from send_files import send_files

HEADER = 64
PORT = 5010
BUFFER_SIZE = 4096
FORMAT = 'utf-8'
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
send_files(client, ["data.csv"])
send_files(client, ["server-data.csv"])

client_buffer = Buffer(client)

while True:
    file_name = client_buffer.get_utf8()
    if not file_name:
        break
    file_name = os.path.join('files', file_name)
    file_size = int(client_buffer.get_utf8())

    with open(file_name, 'wb') as f:
        remaining = file_size
        while remaining:
            chunk_size = BUFFER_SIZE if remaining >= BUFFER_SIZE else remaining
            print(chunk_size)
            chunk = client_buffer.get_bytes(chunk_size)
            if not chunk:
                break
            f.write(chunk)
            remaining -= len(chunk)
        if remaining:
            print('File incomplete.  Missing', remaining, 'bytes.')
        else:
            print('File received successfully.')
