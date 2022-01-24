import path_utilities
import shutil


# This function force updates Project Zomboid Server Steam Workshop Content File from the Client folder with any
# updated mods that don't match with the Server's mods that have not been updated yet and throws the ever annoying
# error message "Workshop item version different than server's".
def force_update():
    shutil.copy(path_utilities.client_workshop_path_input(), path_utilities.server_workshop_path_input())
