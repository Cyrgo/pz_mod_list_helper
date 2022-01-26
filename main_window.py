import mod_update_fixer
import output_utilities
import path_utilities
import tkinter
from tkinter import *

# Main window is created, name, icon and size are all specified.
main_window = tkinter.Tk()
main_window.wm_iconbitmap('images/icon.ico')
main_window.title("PZ Server Mod Force Updater")
main_window.geometry("380x140+10+20")

# Variables to be used are declared.
drive_var = tkinter.StringVar()
drive_entry = tkinter.Entry(main_window, textvariable=drive_var)


# This function is called after the Spiffo submit button is clicked, input is taken and used to call path utility
# methods to create the two paths needed for the force update function to use to force update mods.
def submit():
    output_utilities.please_wait()

    drive_name = drive_entry.get()

    file_path = path_utilities.client_workshop_path(drive_name)

    folder_path = path_utilities.server_workshop_path(drive_name)

    file_folder = mod_update_fixer.force_update(file_path, folder_path)

    output_utilities.alert(file_folder)


# Main window widgets are declared and given the necessary info to function in the main window.
main_lbl = Label(main_window, text=output_utilities.welcome_message(), font=("calibre", 10, "bold"))
spiffo = PhotoImage(file="images/spiffo-button.png")
submit_btn = tkinter.Button(main_window, command=submit, image=spiffo)

# Main window widgets are placed on the window with .pack so that they stay in their assigned position interdependent
# of window size.
main_lbl.pack(side="top")
drive_entry.pack(side="top")
submit_btn.pack(side="bottom")

# The main window is run.
main_window.mainloop()
