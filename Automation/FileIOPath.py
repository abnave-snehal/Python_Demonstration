import os

def main():
    fileName=input("Enter the name of file : ")

    ret=os.path.isabs(fileName)
    
    if(ret == True):
        print("It's Absolute Path.")
    else:
        print("It's Relative Path.")
    



if __name__ == "__main__":
    main()