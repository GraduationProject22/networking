import os
from buffer import Buffer
from send_files import send_files

BUFFER_SIZE = 4096


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connection_buffer = Buffer(conn)
    send_files(conn, ["server-data.csv"])
    connection_buffer.put_utf8("Hello from server")
    while True:
        file_name = connection_buffer.get_utf8()
        if not file_name:
            break
        file_name = os.path.join('files', file_name)
        file_size = int(connection_buffer.get_utf8())

        with open(file_name, 'wb') as f:
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
    print('Connection closed.')
    conn.close()
