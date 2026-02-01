import os

def main():
    fileName=input("Enter the name of file : ")

    if(os.path.exists(fileName)):    
        ret=os.path.isabs(fileName)
        os.remove(fileName)
        print("File gets deleted.")
    else:
        print("There is no such file.")

if __name__ == "__main__":
    main()