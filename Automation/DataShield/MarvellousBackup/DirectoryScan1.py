import os

def main():
    DirectoryName=input("Enter the name of directory : ")

    print("Contents of the directory are : ")

    for folderName,subFolderName,Filename in os.walk(DirectoryName):
        print("Folder name : ",folderName)
        
        for subF in subFolderName:
            print("SubFolders name : ",subF)
        
        for fname in Filename:
            print("File name : ",fname)

if __name__ == "__main__":
    main()