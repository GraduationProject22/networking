import socket
from multiprocessing import Process
from utils.buffer import Buffer
from utils.send_files import send_files
from utils.add_ip_address import add_ip_address
from utils.receive_from_server import receive_from_server
from utils.get_latest_file import get_latest_file
from utils.receive_from_uart import receive_from_uart
from utils.get_last_edit_time import get_last_edit_time

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


def uart_handler():
    while True:
        old_latest_file = get_latest_file('files')
        old_latest_file_edit_time = get_last_edit_time(
            "files/" + old_latest_file)

        receive_from_uart()

        # ! For testing
        sleep(2)
        #create_dummy_json_file()

        new_latest_file = get_latest_file('files')
        new_latest_file_edit_time = get_last_edit_time(
            "files/" + new_latest_file)
        # TODO Remove next print lines
        print("old_latest_file: " + old_latest_file)
        print("old_latest_file_edit_time: " + str(old_latest_file_edit_time))
        print("new_latest_file: " + new_latest_file)
        print("new_latest_file_edit_time: " + str(new_latest_file_edit_time))

        if old_latest_file_edit_time != new_latest_file_edit_time:
            print("Different file!")
            # add_ip_address("files/" + new_latest_file)
            send_files(client, ["file_sending_client2.json"])


def server_handler():
    while True:
        receive_from_server(client_buffer)


p1 = Process(target=uart_handler)
p1.start()
p2 = Process(target=server_handler)
p2.start()
p1.join()
p2.join()
