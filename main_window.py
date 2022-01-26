import mod_update_fixer
import output_utilities
import path_utilities
import tkinter
from tkinter import *


main_window = tkinter.Tk()
main_window.wm_iconbitmap('images/icon.ico')
main_window.title("PZ Server Mod Force Updater")
main_window.geometry("380x140+10+20")

drive_var = tkinter.StringVar()
drive_entry = tkinter.Entry(main_window, textvariable=drive_var)


def submit():
    output_utilities.please_wait()

    drive_name = drive_entry.get()

    file_path = path_utilities.client_workshop_path(drive_name)

    folder_path = path_utilities.server_workshop_path(drive_name)

    file_folder = mod_update_fixer.force_update(file_path, folder_path)

    output_utilities.alert(file_folder)


main_lbl = Label(main_window, text=output_utilities.welcome_message(), font=("calibre", 10, "bold"))

spiffo = PhotoImage(file="images/spiffo-button.png")
submit_btn = tkinter.Button(main_window, command=submit, image=spiffo)

main_lbl.pack(side="top")
drive_entry.pack(side="top")
submit_btn.pack(side="bottom")

main_window.mainloop()
