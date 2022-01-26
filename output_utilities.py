from tkinter import messagebox


def welcome_message():
    return str("Type the name of your drive where your SteamLibrary is in." +
               "\n" +
               "Click on Spiffo to force update your Server mods!")


def alert(some_string):
    messagebox.showinfo("Hello", some_string)


def please_wait():
    messagebox.showinfo("Running", "Please wait.")