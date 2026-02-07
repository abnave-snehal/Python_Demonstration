#Command line input 

import psutil
import sys
import os

def createLog(folderName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)

def main():
    border="-"*50
    print(border)
    print("----- Marvellous Platform Surveillance System ----")
    print(border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or "--H"):
            print("This script is use to : ")
            print("1: Create automatic logs")
            print("2: Execute periodically")
            print("3: Sends mail with log")
            print("4: Store information about processes")
            print("5: Store information about CPU")
            print("6: Store infromation about RAM usage")
            print("7: Store information about secondary storage")
        elif(sys.argv[2] == "--u" or "--U"):
            print("Use the automation script as")
            print("ScriptNAme.py Timeinterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is nno such option")
            print("Please use --h or --u to get more details")

    #python Demo.py 5 Marvellous 
    elif(len(sys.argv)==3):
        print("Inside projects logic : ")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])
        createLog(sys.argv[2])
    else:
         print("Invalid number of command line arguments")
         print("Unable to proceed as there is nno such option")
         print("Please use --h or --u to get more details")

    print(border)
    print("--------- Thank You For Using Our Script --------- ")
    print(border)

if __name__ == "__main__":
    main()