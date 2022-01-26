import os


def find_workshop_file_path(filename, drive):

    for root, dirs, files in os.walk(drive + ":\\"):
        if filename in files:
            return root + "\\" + filename


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
