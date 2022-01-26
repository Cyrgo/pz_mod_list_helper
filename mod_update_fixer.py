import shutil


# This function force updates Project Zomboid Server Steam Workshop Content File from the Client folder with any
# updated mods that don't match with the Server's mods that have not been updated yet and throws the ever annoying
# error message "Workshop item version different than server's".
def force_update(file_path, folder_path):
    shutil.copy(file_path, folder_path)
    return file_path + "\n" + folder_path
