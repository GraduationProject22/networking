import socket
from multiprocessing import Process
from utils.buffer import Buffer
from utils.send_files import send_files
from utils.add_ip_address import add_ip_address
from utils.receive_from_server import receive_from_server
from utils.get_latest_file import get_latest_file
from utils.receive_from_uart import receive_from_uart
from utils.get_last_edit_time import get_last_edit_time


HEADER = 64
PORT = 5030
SERVER = "192.168.1.5"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)


client_buffer = Buffer(client)


def uart_handler():
    while True:

        receive_from_uart()

        add_ip_address("files/" + "file_sending_client2.json")
        send_files(client, ["file_sending_client2.json"])


def server_handler():
    while True:
        receive_from_server(client_buffer)


if __name__ == "__main__":
    p1 = Process(target=uart_handler)
    p1.start()
    p2 = Process(target=server_handler)
    p2.start()
    p1.join()
    p2.join()
