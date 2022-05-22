import socket
from multiprocessing import Process
from utils.buffer import Buffer
from utils.send_files import send_files
from utils.add_ip_address import add_ip_address
from utils.receive_from_server import receive_from_server
from utils.get_latest_file import get_latest_file
from utils.receive_from_uart import receive_from_uart
from utils.get_last_edit_time import get_last_edit_time
from utils.read_file import read_file
from utils.send_files import send_files
# ! For testing
from utils.write_json_file import write_json_file
from time import sleep

HEADER = 64
PORT = 5020
SERVER = "192.168.1.9"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)


client_buffer = Buffer(client)


# ! For testing

def create_dummy_json_file():

    # generate random integer values
    from random import seed
    from random import randint
    # seed random number generator
    seed(1)
    # generate some integers
    value = randint(0, 10)
    write_json_file("files/new_test.json", "a={},b=3, c=4.".format(value))




def server_handler():
    while True:
        send_files(client, ["file_sending_client1.json"])
        sleep(2)
        receive_from_server(client_buffer)

server_handler()
