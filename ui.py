import tkinter
from tkinter import *
from tkinter import messagebox

import output_utilities

main_window = tkinter.Tk()
main_window.wm_iconbitmap('images/icon.ico')
main_window.title("PZ Server Mod Force Updater")
main_window.geometry("380x140+10+20")

drive_var = tkinter.StringVar()
drive_entry = tkinter.Entry(main_window, textvariable=drive_var)


def alert():
    messagebox.showinfo("Hello", drive_entry.get())


def submit():

    drive_name = drive_entry.get()

    alert()

    return drive_name


main_lbl = Label(main_window, text=output_utilities.welcome_message(), font=("calibre", 10, "bold"))

spiffo = PhotoImage(file="images/spiffo-button.png")
submit_btn = tkinter.Button(main_window, command=submit, image=spiffo)

main_lbl.pack(side="top")
drive_entry.pack(side="top")
submit_btn.pack(side="bottom")

main_window.mainloop()
