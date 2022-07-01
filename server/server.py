import os
import socket
import threading
from utils.handle_client import handle_client
from utils.observable import Observable
import tkinter as tk
from utils.get_ip_address import get_ip_address

# Constants
PORT = 5030
IP = get_ip_address()
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (IP, PORT)
FORMAT = 'utf-8'


try:
    os.mkdir('files')
except FileExistsError:
    pass


def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    serverObservable = Observable()
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")

    thread = threading.Thread(target=gui)
    thread.start()
    global vehicles_StringVar
    global subscribers
    subscribers = []
    global subscribers_StringVar
    number_of_vehicles = 0
    global log
    log = []
    global log_StringVar
    while True:
        conn, addr = server.accept()
        number_of_vehicles += 1
        subscribers.append(addr[0])
        subscribers_StringVar.set(value=subscribers)
        vehicles_StringVar.set("Vehicles: " + str(number_of_vehicles))
        log.append("{} connected".format(addr[0]))
        log_StringVar.set(value=log)
        thread = threading.Thread(
            target=handle_client, args=(conn, addr, serverObservable))
        thread.start()


def gui():
    global vehicles_StringVar
    global subscribers_StringVar
    global log_StringVar

    window = tk.Tk()

    log_StringVar = tk.StringVar()
    log_StringVar.set([])

    vehicles_StringVar = tk.StringVar()
    vehicles_StringVar.set("Vehicles: 0")

    ip_StringVar = tk.StringVar()
    ip_StringVar.set("IP: {}".format(IP))

    port_StringVar = tk.StringVar()
    port_StringVar.set("Port: {}".format(PORT))

    subscribers_StringVar = tk.StringVar()
    subscribers_StringVar.set([])

    frame1 = tk.Frame(master=window, width=200,
                      borderwidth=1, relief=tk.RAISED,)
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    frame2 = tk.Frame(master=window, width=100,
                      borderwidth=1, relief=tk.RAISED,)
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    frame1.columnconfigure(0, weight=1)
    frame1.rowconfigure(1, weight=1)

    window.title("Server")
    window.geometry('800x600')

    tk.Label(frame1, text="Log",
             font=("Arial, 20")).grid(row=0, column=0, sticky="w")
    tk.Listbox(frame1, listvariable=log_StringVar).grid(
        row=1, column=0, sticky="nsew")

    frame2.rowconfigure(3, weight=1)
    frame2.columnconfigure(0, weight=1)

    tk.Label(frame2, textvariable=ip_StringVar,
             font=("Arial, 20")).grid(row=0, column=0, sticky="w")
    tk.Label(frame2, textvariable=port_StringVar,
             font=("Arial, 20")).grid(row=1, column=0, sticky="w")
    tk.Label(frame2, textvariable=vehicles_StringVar,
             font=("Arial, 20")).grid(row=2, column=0, sticky="w")
    tk.Listbox(frame2, listvariable=subscribers_StringVar).grid(
        row=3, column=0, columnspan=5, sticky="nsew")

    window.mainloop()


print("[STARTING] server is starting...")

start()
