from tkinter import messagebox


#  This function returns a welcome message to users.
def welcome_message():
    return str("Type the name of your drive where your SteamLibrary is in." +
               "\n" +
               "Click on Spiffo to force update your Server mods!")


#  This function returns an info alert with a string that is provided to the function.
def alert(some_string):
    messagebox.showinfo("Hello", some_string)


# This function displays a message box to let the user know the program is running.
def please_wait():
    messagebox.showinfo("Running", "Please wait.")