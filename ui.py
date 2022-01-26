import tkinter
from tkinter import *
from tkinter import messagebox

import output_utilities

main_window = tkinter.Tk()
main_window.wm_iconbitmap('images/icon.ico')
main_window.title("PZ Server Mod Force Updater")
main_window.geometry("380x140+10+20")


def alert():
    messagebox.showinfo("Hello", "World")


def submit():

    alert()


main_lbl = Label(main_window, text=output_utilities.welcome_message(), font=("calibre", 10, "bold"))

drive_var = tkinter.StringVar()
drive_entry = tkinter.Entry(main_window, textvariable=drive_var)

spiffo = PhotoImage(file="images/spiffo-button.png")
submit_btn = tkinter.Button(main_window, text="Submit", command=submit, image=spiffo)

main_lbl.pack(side="top")
drive_entry.pack(side="top")
submit_btn.pack(side="bottom")

main_window.mainloop()
