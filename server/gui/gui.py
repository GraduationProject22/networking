import json
from os import listdir
import threading
import tkinter as tk


list = ["Longitude", "Latitude", "Speed", "Ax", "Ay", "Angle", "Vx", "Vy"]


def main():
    threading.Thread(target=gui).start()
    global server_ip_StringVar
    global server_port_StringVar
    global server_vehicles_StringVar
    global vehicle_one_StringVar
    global vehicle_two_StringVar
    while True:
        server_info_file = open("./files/server_info", "r")
        server_info_obj = json.load(server_info_file)
        server_info_file.close()
        server_ip_StringVar.set("IP: " + server_info_obj["ip"])
        server_port_StringVar.set("PORT: " + str(server_info_obj["port"]))
        server_vehicles_StringVar.set(
            "Vehicles: " + str(server_info_obj["vehicles"]))
        ips = []
        for file in listdir("./files"):
            if file != "server_info":
                f = open("./files/" + file, "r")
                obj = json.load(f)
                f.close()
                if obj["ip"] not in ips:
                    ips.append(obj["ip"])
        count = 0
        vehicle_one_data = []
        vehicle_two_data = []
        for ip in ips:
            f = open("./files/" + ip + ".json", "r")
            obj = json.load(f)
            f.close()
            if count == 0:
                for key in obj:
                    if key == "D":
                        for index, item in obj["D"].split(","):
                            vehicle_one_data.append(list[index] + item)

                vehicle_one_StringVar.set(vehicle_one_data)
            if count == 1:
                for key in obj:
                    vehicle_two_data.append(key + ": " + str(obj[key]))
                vehicle_two_StringVar.set(vehicle_two_data)
            count += 1


def gui():

    window = tk.Tk()
    global vehicle_one_StringVar
    global vehicle_two_StringVar
    global server_ip_StringVar
    global server_port_StringVar
    global server_vehicles_StringVar

    server_ip_StringVar = tk.StringVar()
    server_port_StringVar = tk.StringVar()
    server_vehicles_StringVar = tk.StringVar()
    vehicle_one_StringVar = tk.StringVar()
    vehicle_two_StringVar = tk.StringVar()

    server_ip_StringVar.set("")
    server_port_StringVar.set("")
    server_vehicles_StringVar.set("")
    vehicle_one_StringVar.set([])
    vehicle_two_StringVar.set([])

    frame1 = tk.Frame(master=window, width=400,
                      borderwidth=1, relief=tk.RAISED,)
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    frame2 = tk.Frame(master=window, width=400,
                      borderwidth=1, relief=tk.RAISED,)
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    tk.Label(master=frame1, textvariable=server_ip_StringVar).pack()
    tk.Label(master=frame1, textvariable=server_port_StringVar).pack()
    tk.Label(master=frame1, textvariable=server_vehicles_StringVar).pack()
    tk.Label(master=frame1, text="Warning",
             font=("Arial", 22), fg="red").pack()

    tk.Label(master=frame2, text="Vehicle 1").pack()
    tk.Listbox(master=frame2, listvariable=vehicle_one_StringVar).pack()

    tk.Label(master=frame2, text="Vehicle 2").pack()
    tk.Listbox(master=frame2, listvariable=vehicle_two_StringVar).pack()

    frame1.columnconfigure(0, weight=1)
    frame1.rowconfigure(1, weight=1)

    window.title("Server")
    window.geometry('800x600')

    window.mainloop()


main()
