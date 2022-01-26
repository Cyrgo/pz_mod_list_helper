import tkinter
from tkinter import *
from tkinter import messagebox

import output_utilities

main_window = tkinter.Tk()
main_window.wm_iconbitmap('images/icon.ico')
main_window.title("PZ Server Mod Force Updater")
main_window.geometry("360x140+10+20")

# Variables to hold string paths.
client_workshop_file_path = tkinter.StringVar()
server_workshop_folder_path = tkinter.StringVar()


def alert():
    messagebox.showinfo("Hello", "World")


def submit():
    cwfp = client_workshop_file_path.get()
    swfp = server_workshop_folder_path.get()

    print(cwfp + swfp)

    client_workshop_file_path.set("")
    server_workshop_folder_path.set("")
    alert()


spiffo = PhotoImage(file="images/spiffo-button.png")
submit_btn = tkinter.Button(main_window, text="Submit", command=submit, image=spiffo)

main_lbl = Label(main_window, text=output_utilities.welcome_message(), font=("calibre", 10, "bold"))
main_lbl.pack(side="top")
submit_btn.pack(side="bottom")

main_window.mainloop()
