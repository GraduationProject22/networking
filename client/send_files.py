from buffer import Buffer
import os


def send_files(client, files):
    client_buffer = Buffer(client)
    for file in files:
        client_buffer.put_utf8(file)
        file_name = os.path.join('files', file)

        # get the file size
        file_size = os.path.getsize(file_name)

        client_buffer.put_utf8(str(file_size))

        # start sending the file
        with open(file_name, "rb") as f:
            client_buffer.put_bytes(f.read())
