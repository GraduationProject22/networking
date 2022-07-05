import tkinter as tk


def gui():
    window = tk.Tk()

    frame1 = tk.Frame(master=window, width=400,
                      borderwidth=1, relief=tk.RAISED,)
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    frame2 = tk.Frame(master=window, width=400,
                      borderwidth=1, relief=tk.RAISED,)
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    frame1.columnconfigure(0, weight=1)
    frame1.rowconfigure(1, weight=1)

    window.title("Server")
    window.geometry('800x600')

    window.mainloop()


gui()
