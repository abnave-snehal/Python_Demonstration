import hashlib
import os

def CalculateChkSum(fileName):
    fobj=open(fileName,"rb")   #read in binary mode

    hobj=hashlib.md5()

    Buffer=fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName="Marvellous"):
    ret=False

    ret=os.path.exists(DirectoryName)

    if(ret == False):
        print("There is no such directory : ")
        return
    
    ret=os.path.isdir(DirectoryName)

    if(ret == False):
        print("It's not a directory : ")

    for folderName,subFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(folderName,fname)
            checkSum=CalculateChkSum(fname)

            print(f"File Name : {fname} Checksum : {checkSum}")

def main():

   DirectoryWatcher()

if __name__ == "__main__":
    main()