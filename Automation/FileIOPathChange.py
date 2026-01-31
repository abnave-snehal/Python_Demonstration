import os

def main():
    fileName=input("Enter the name of file : ")

    ret=os.path.isabs(fileName)
    
    if(ret == True):
        print("It's Absolute Path.")
    else:
        print("It's Relative Path.")
        NewPath=os.path.abspath(fileName)
        print("Updated path : ",NewPath)
    



if __name__ == "__main__":
    main()