from multiprocessing import connection
import os
import socket
import threading
from utils.handle_client import handle_client
from utils.observable import Observable

# Constants
PORT = 5020
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

try:
    os.mkdir('files')
except FileExistsError:
    pass


def start():
    # print(max(["files/" + file for file in os.listdir("files")],
    #       key=os.path.getctime))
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
