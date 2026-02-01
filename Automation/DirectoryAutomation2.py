import sys
import os

def directoryScanner(DirName="Marvellous"):  # Default Argument
    ret=False

    ret=os.path.exists(DirName)
    if(ret == False):
        print("There is no such directory.")
        return
    
    
    ret=os.path.isdir(DirName)
    if(ret == False):
        print("It is not a directory.")
        return
    
    for folderName,subFolder,fileName in os.walk(DirName):
        for Fname in fileName:
            print("File Name : ",Fname)
            print("File Size : ",os.path.getsize(Fname))  # Path Issue


def main():
    Border="-"*50
    print(Border)
    print("---------- Marvellous Directory Automation ----------")
    print(Border)

    if(len(sys.argv) !=2):
        print("Invalid number of arguments:")
        print("Please sepcifiy the name of directory :")
        return

    directoryScanner(sys.argv[1])


if __name__ == "__main__":
    main()