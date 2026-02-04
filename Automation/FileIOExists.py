import os

def main():
    fileName=input("Enter the name of file : ")

    ret=os.path.exists(fileName)
    
    if(ret == True):
        fobj=open(fileName,"r")
        print("File gets successfully opend.")
    else:
        print("There is no such file. ")
    
if __name__ == "__main__":
    main()