# This function takes in string path of Project Zomboid Server Config Ini and returns it to be used.
def ini_path_input():
    print("Enter the path of your Project Zomboid Server Configuration ini file.")
    print("Best to open the file from file explorer,")
    print("copy paste the address, and add the Server Configuration ini file name.")
    print("Example: C:\\Users\\cyrgo\\Zomboid\\Server\\31 Days Later-With Adi.ini")
    ini_path = input()
    return ini_path


# This function takes in the string path of Project Zomboid Client Steam Workshop Content File and returns it to be
# used.
def client_workshop_path_input():
    print("Enter the path of your Project Zomboid client Steam Workshop file.")
    print("Best to open the file from file explorer,")
    print("copy paste the address, and add the .acf file extension.")
    print("Example: D:\\SteamLibrary\\steamapps\\workshop\\appworkshop_108600.acf")
    acf_path = input()
    return acf_path


# This function takes in the string path of Project Zomboid Server Steam Workshop Content Folder and returns it to be
# used.
def server_workshop_path_input():
    print("Enter the path of your Project Zomboid server Steam Workshop folder.")
    print("Best to open the folder from file explorer,")
    print("and copy paste the address.")
    print("Example: D:\\SteamLibrary\\steamapps\\common\\ProjectZomboid\\steamapps\\workshop")
    workshop_folder_path = input()
    return workshop_folder_path
