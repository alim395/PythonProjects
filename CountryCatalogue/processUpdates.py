from catalogue import CountryCatalogue
from country import Country

def processUpdates(cntryFileName,updateFileName):
    while True:
        try: # Checks if file exists
            cntry = open(cntryFileName, 'r', encoding='utf-8', errors='ignore')
            cntry.close()
            break
        except FileNotFoundError:
            print("Country file could not be found.")  # prompts user that file name was wrong/not found
            quitting = input("Would you like to quit? [Y/N]")
            if (quitting != "N") and (quitting != "n"): # creates an output file but shows that update was unsuccessful
                f = open("output.txt", "w")
                f.write("Update Unsuccessful")
                f.close()
                return False  # allows the user to exit the while loop
            else:
                cntryFileName = input("Enter correct file name:")  # prompts user for correct file name
            continue
    cD = CountryCatalogue(cntryFileName)
    while True:
        try: # Checks if file exists
            update = open(updateFileName, 'r', encoding='utf-8', errors='ignore')
            for line in update:
                uFile = line.rstrip("\n")
            break
        except FileNotFoundError:
            print("Update file could not be found.")  # prompts user that file name was wrong/not found
            quitting = input("Would you like to quit? [Y/N]")
            if (quitting != "N") and (quitting != "n"): # creates an output file but shows that update was unsuccessful
                f = open("output.txt", "w")
                f.write("Update Unsuccessful")
                f.close()
                return False  # allows the user to exit the while loop
            else:
                updateFileName = input("Enter correct file name:")  # prompts user for correct file name
            continue

    # Validating the updates
    update = open(updateFileName, 'r', encoding='utf-8', errors='ignore')
    rawUpdate = update.readlines()
    for n in range(0, len(rawUpdate)):
        uVars = rawUpdate[n].strip('\n').split(';')
        uName = ""
        uArea = ""
        uPop = ""
        uCont = ""
        u1 = ""
        u2 = ""
        u3 = ""
        try:
            uName = uVars[0]
            u1 = uVars[1].strip('\n')
            u2 = uVars[2].strip('\n')
            u3 = uVars[3].strip('\n')
        except:
            pass
        try:
            # checking if area is being updated and valid
            if 'A=' in u1:
                uArea = u1.lstrip('A=')
                uAT = uArea.strip(', ')
                uAT = '{:,}'.format(uAT)
                if uArea != uAT:
                    raise ValueError()
            elif 'A=' in u2:
                uArea = u2.lstrip('A=')
                uAT = uArea.strip(',')
                uAT = '{:,}'.format(uAT)
                if uArea != uAT:
                    raise ValueError()
            elif 'A=' in u3:
                uArea = u3.lstrip('A=')
                uAT = uArea.strip(',')
                uAT = '{:,}'.format(uAT)
                if uArea != uAT:
                    raise ValueError()
        except:
            pass
        try:
            # checking if population is being updated and valid
            if 'P=' in u1:
                uPop = u1.lstrip('P=')
                uPT = uArea.strip(',')
                uPT = '{:,}'.format(uPT)
                if uPop != uPT:
                    raise ValueError()
            elif 'P=' in u2:
                uPop = u2.lstrip('P=')
                uPT = uArea.strip(',')
                uPT = '{:,}'.format(uPT)
                if uPop != uPT:
                    raise ValueError()
            elif 'P=' in u3:
                uPop = u3.lstrip('P=')
                uPT = uArea.strip(',')
                uPT = '{:,}'.format(uPT)
                if uPop != uPT:
                    raise ValueError()

            # set of valid continents for validation
            validCont = {'Africa', 'Antarctica', 'Arctic', 'Asia', 'Europe', 'North America', 'South America'}
        except:
            pass
            # checking if continent is being updated and valid
        try:
            if 'C=' in u1:
                uCont = u1.lstrip('C=')
                uCT = uCont.lower()
                UCT = uCont.title()
                if uCT not in validCont:
                    raise ValueError()
            elif 'C=' in u2:
                uCont = u2.lstrip('C=')
                uCT = uCont.lower()
                UCT = uCont.title()
                if uCT not in validCont:
                    raise ValueError()
            elif 'C=' in u3:
                uCont = u3.lstrip('C=')
                uCT = uCont.lower()
                UCT = uCont.title()
                if uCT not in validCont:
                    raise ValueError()
        except:
            pass

        #Checking if country exists
        if uName not in cD.countryCat.keys():
            cD.addCountry(uName,uPop,uArea,uCont)

        #updating...
        if uPop != "":
            cD.setPopulationOfCountry(uName,uPop)
        if uArea != "":
            cD.setAreaOfCountry(uName,uArea)
        if uCont != "":
            cD.setContinentOfCountry(uName,uCont)

    #Saving
    cD.saveCountryCatalogue("output.txt")
    return True
