import ini_grabber

ini = ini_grabber.serverConfig.readlines()

# Mod Names and Workshop Ids are captured as strings from ini file.
modNames = ini[19]
ids = ini[60]

# Mod Names and Workshop Ids are split by ";", and converted into lists.
mnSplit = modNames.split(";")
idSplit = ids.split(";")

# Empty list is created for Mod Names to remove "Mods=" from the first mod name in the list,
# and the new line is removed from the last mod name in the list.
mnsClean = []
for mods in mnSplit:
    modsLineZero = mods.replace("Mods=", "")
    mnsClean.append(modsLineZero)
modsLineLast = mnSplit[-1].replace("\n", "")
mnsClean.pop()
mnsClean.append(modsLineLast)

# Empty list is created for Workshop Ids to remove "WorkshopItems=" from the first workshop id in the list,
# and the new line is removed from the last workshop id in the list.
idsClean = []
for mods in idSplit:
    modsLineZero = mods.replace("WorkshopItems=", "")
    idsClean.append(modsLineZero)
modsLineLast = idSplit[-1].replace("\n", "")
idsClean.pop()
idsClean.append(modsLineLast)

# Each list length is counted.
mnCount = len(mnsClean)
idCount = len(idsClean)

# The difference between each length is calculated.
# Useful for detecting Mod and Workshop Id lists that don't equal each other in length.
diff = mnCount - idCount

# Console string output of the difference in both lists.
if mnCount != idCount:
    print("You have " + str(mnCount) + " mods installed,")
    if mnCount >= 2:
        print("but only " + str(idCount) + " Workshop Ids.")
    else:
        print("but only " + str(idCount) + " Workshop Id.")
    if diff >= 2:
        print("You have a few mods that have included mods that are messing up mod id association.")
    else:
        print("You have one mod that has more included mods that are messing up mod id association.")
else:
    print("No Id issues detected.")

# A loop to add dashes to the Id List depending on the difference of the Mod Name List and Id List.
# This is done so that a proper table can be printed.
if idCount < mnCount:
    for i in range(diff):
        idsClean.append(" - ")

# Both lists are printed side by side to the console,
# Though the accuracy of the ids to mod names is not accurate if some mods include more mods
# and only one id is given to both mods in the Workshop Id line of the ini.
sbsList = "\n".join("{:>5} : {:5}".format(x, y) for x, y in zip(mnsClean, idsClean))
print(sbsList)
print("It is likely that the Ids might not be assigned to the right mod if a mod includes more mods.")
print("Only one Id is given to a mod and the included mods are not given an empty space.")
print("As a result, the server fails to launch because it gets confused that Mods and Ids don't match.")
