import json
import shutil
import os
from utils.read_file import read_file
from utils.buffer import Buffer
from utils.send_files import send_files

BUFFER_SIZE = 4096


def handle_client(conn, addr, serverObservable):
    print(f"[NEW CONNECTION] {addr} connected.")
    connection_buffer = Buffer(conn)
    serverObservable.subscribe([conn, addr[0]])
    while True:
        file_name = connection_buffer.get_utf8()
        if not file_name:
            break
        full_file_name = os.path.join('files', file_name)
        file_size = int(connection_buffer.get_utf8())

        with open(full_file_name, 'wb') as f:
            remaining = file_size
            while remaining:
                chunk_size = BUFFER_SIZE if remaining >= BUFFER_SIZE else remaining
                print(chunk_size)
                chunk = connection_buffer.get_bytes(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                remaining -= len(chunk)
            if remaining:
                print('File incomplete.  Missing', remaining, 'bytes.')
            else:
                print('File received successfully.')
        file_ip = json.loads(read_file(full_file_name))["ip"]
        shutil.copyfile(full_file_name, os.path.join(
            'gui/files/', file_name))
        serverObservable.notify(file_name, file_ip)
    serverObservable.unsubscribe(conn)
    print('Connection closed.')
    conn.close()
