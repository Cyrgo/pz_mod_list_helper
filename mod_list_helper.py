import output_utilities
import path_utilities


def mod_list_diagnostic():
    # Opens the ini from its file location, with read only access.
    server_config = open(path_utilities.ini_path_input(), "r")
    ini = server_config.readlines()
    # Mod Names and Workshop Ids are captured as strings from ini file.
    mod_names = ini[19]
    ids = ini[60]
    # Mod Names and Workshop Ids are split by ";", and converted into lists.
    mn_split = mod_names.split(";")
    id_split = ids.split(";")
    # Empty list is created for Mod Names to remove "Mods=" from the first mod name in the list,
    # and the new line is removed from the last mod name in the list.
    mns_clean = []
    for mods in mn_split:
        mods_line_zero = mods.replace("Mods=", "")
        mns_clean.append(mods_line_zero)
    mods_line_last = mn_split[-1].replace("\n", "")
    mns_clean.pop()
    mns_clean.append(mods_line_last)
    # Empty list is created for Workshop Ids to remove "WorkshopItems=" from the first workshop id in the list,
    # and the new line is removed from the last workshop id in the list.
    ids_clean = []
    for mods in id_split:
        mods_line_zero = mods.replace("WorkshopItems=", "")
        ids_clean.append(mods_line_zero)
    mods_line_last = id_split[-1].replace("\n", "")
    ids_clean.pop()
    ids_clean.append(mods_line_last)
    # Each list length is counted.
    mn_count = len(mns_clean)
    id_count = len(ids_clean)
    # The difference between each length is calculated.
    # Useful for detecting Mod and Workshop Id lists that don't equal each other in length.
    diff = mn_count - id_count
    # Console string output of the difference in both lists.
    if mn_count != id_count:
        print("You have " + str(mn_count) + " mods installed,")
        if mn_count >= 2:
            print("but only " + str(id_count) + " Workshop Ids.")
        else:
            print("but only " + str(id_count) + " Workshop Id.")
        if diff >= 2:
            print("You have a few mods that have included mods that are messing up mod id association.")
            output_utilities.separator()
        else:
            print("You have one mod that has more included mods that are messing up mod id association.")
            output_utilities.separator()

    else:
        print("No Id issues detected.")
        output_utilities.separator()
    # A loop to add dashes to the Id List depending on the difference of the Mod Name List and Id List.
    # This is done so that a proper table can be printed.
    if id_count < mn_count:
        for i in range(diff):
            ids_clean.append(" - ")
    # Both lists are printed side by side to the console,
    # Though the accuracy of the ids to mod names is not accurate if some mods include more mods
    # and only one id is given to both mods in the Workshop Id line of the ini.
    sbs_list = "\n".join("{:>5} : {:5}".format(x, y) for x, y in zip(mns_clean, ids_clean))
    print(sbs_list)
    output_utilities.separator()
    print("It is likely that the Ids might not be assigned to the right mod if a mod includes more mods.")
    print("Only one Id is given to a mod and the included mods are not given an empty space.")
