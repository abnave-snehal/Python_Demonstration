import os
def DirectoryScanner(DirectoryName="Marvellous"):
    ret=os.path.exists(DirectoryName)

    if(ret == False):
        print("There is no such directory : ")
        return              # return to main()

    ret=os.path.isdir(DirectoryName)
    if(ret == False):
        print("Unable to scan as it's not a directory.")
        return
    
    print("Contents of the directory are : ")

    for folderName,subFolderName,Filename in os.walk(DirectoryName):
        print("Folder name : ",folderName)
        
        for subF in subFolderName:
            print("SubFolders name : ",subF)
        
        for fname in Filename:
            print("File name : ",fname)

def main():
    DirectoryName=input("Enter the name of directory : ")

    DirectoryScanner(DirectoryName)

if __name__ == "__main__":
    main()