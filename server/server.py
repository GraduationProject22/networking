import socket
import threading
import tqdm

HEADER = 64
PORT = 5010
SERVER = socket.gethostbyname(socket.gethostname())
BUFFER_SIZE = 4096
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:

        msg = conn.recv(BUFFER_SIZE).decode(FORMAT)

        if msg:
            filename = msg.split(" ")[0]
            print(msg.split(" "))
            with open(filename, "wb") as f:
                while True:
                    # read 1024 bytes from the socket (receive)
                    bytes_read = conn.recv(BUFFER_SIZE)
                    if not bytes_read:
                        # nothing is received
                        # file transmitting is done
                        break
                    # write to the file the bytes we just received
                    f.write(bytes_read)
                    f.close()

        if msg == DISCONNECT_MESSAGE:
            connected = False
        # print(f"[{addr}] {msg}")
        # conn.send("Msg received".encode(FORMAT))


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


print("[STARTING] server is starting...")
start()
