from utils.buffer import Buffer
import os


def send_files(socket, files):
    server_buffer = Buffer(socket)
    for file in files:
        server_buffer.put_utf8(file)
        file_name = os.path.join('files', file)

        # get the file size
        file_size = os.path.getsize(file_name)

        server_buffer.put_utf8(str(file_size))

        # start sending the file
        with open(file_name, "rb") as f:
            server_buffer.put_bytes(f.read())
