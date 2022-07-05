import os
import socket
import threading
from utils.handle_client import handle_client
from utils.observable import Observable
from utils.get_ip_address import get_ip_address

# Constants
PORT = 5040
SERVER = socket.gethostbyname(socket.gethostname())

ADDRESS = ('192.168.1.5', PORT)
FORMAT = 'utf-8'

server_info_obj = {
    PORT: PORT,
    SERVER: SERVER,
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

try:
    os.mkdir('files')
except FileExistsError:
    pass


def start():
    serverObservable = Observable()
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(
            target=handle_client, args=(conn, addr, serverObservable))
        thread.start()


print("[STARTING] server is starting...")
start()
