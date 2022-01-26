# This function combines input drive name with string path of Project Zomboid Client Steam Workshop Content File and
# returns it to be used.
def client_workshop_path(drive_name):
    return drive_name + ":\\SteamLibrary\\steamapps\\workshop\\appworkshop_108600.acf"


# This function combines input drive name with string path of Project Zomboid Server Steam Workshop Content Folder
# and returns it to be used.
def server_workshop_path(drive_name):
    return drive_name + ":\\SteamLibrary\\steamapps\\common\\ProjectZomboid\\steamapps\\workshop"
