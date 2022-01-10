# This function takes in string path of Project Zomboid Server Config Ini and returns it to be used.
def ini_path_input():
    print("Enter the path of your Project Zomboid Server Configuration ini file.")
    print("Best to open the file from file explorer,")
    print("copy paste the address, and add the Server Configuration ini file name.")
    print("Example: C:\\Users\\cyrgo\\Zomboid\\Server\\Test Server.ini")
    ini_path = input()
    return ini_path
