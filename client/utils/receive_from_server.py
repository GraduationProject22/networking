import os

BUFFER_SIZE = 4096


def receive_from_server(client_buffer):
    file_name = client_buffer.get_utf8()
    file_name = os.path.join('files', "file_receiving_client2.json")
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
