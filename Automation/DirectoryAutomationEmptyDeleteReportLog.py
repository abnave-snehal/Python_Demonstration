import sys
import os

def directoryScanner(DirName="Marvellous"):  # Default Argument
    Border="-"*50
    fobj=open("Marvellous.log","w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a directory cleaner script\n")
    fobj.write(Border+"\n")

    
    ret=False

    ret=os.path.exists(DirName)
    if(ret == False):
        print("There is no such directory.")
        return
    
    
    ret=os.path.isdir(DirName)
    if(ret == False):
        print("It is not a directory.")
        return
    
    fileCount=0
    emptyFileCount=0

    for folderName,subFolder,fileName in os.walk(DirName):
       

        for Fname in fileName:
            fileCount=fileCount+1

            Fname=os.path.join(folderName,Fname)

            if(os.path.getsize(Fname) == 0):   # Empty file
                emptyFileCount=emptyFileCount+1
                os.remove(Fname)

    
    fobj.write("Total Files Scanned : "+str(fileCount)+"\n")
    fobj.write("Totla Empty Files Found : "+str(emptyFileCount)+"\n")
    fobj.write(Border+"\n")
    
    fobj.close()

def main():
    Border="-"*50
    print(Border)
    print("--------- Marvellous Directory Automation --------")
    print(Border)

    if(len(sys.argv) !=2):
        print("Invalid number of arguments:")
        print("Please sepcifiy the name of directory :")
        return

    directoryScanner(sys.argv[1])

    print(Border)
    print("--------- Marvellous Directory Automation --------")
    print(Border)

if __name__ == "__main__":
    main()