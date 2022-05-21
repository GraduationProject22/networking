from utils.buffer import Buffer
import os


def send_files(client, files):
    """
    Sends a list of files in 'files' folder to the server.

    Parameters
    ----------
    client : socket.socket
        The client socket.
    files : list
        The list of files to send.
    """

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
