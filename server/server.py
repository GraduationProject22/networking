import json
import os
import socket
import threading
from utils.handle_client import handle_client
from utils.observable import Observable
from utils.get_ip_address import get_ip_address

# Constants
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (get_ip_address(), PORT)
FORMAT = 'utf-8'

server_info_obj = {
    "port": PORT,
    "ip": SERVER,
}

with open("./gui/files/server_info", 'w') as f:
    f.write(json.dumps(server_info_obj))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

try:
    os.mkdir('files')
except FileExistsError:
    pass


def start():
    vehicles = 0
    serverObservable = Observable()
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        vehicles += 1
        server_info_obj["vehicles"] = vehicles
        with open("./gui/files/server_info", 'w') as f:
            f.write(json.dumps(server_info_obj))
        thread = threading.Thread(
            target=handle_client, args=(conn, addr, serverObservable))
        thread.start()


print("[STARTING] server is starting...")
start()
