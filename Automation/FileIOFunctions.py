import os

def main():
    fileName=input("Enter the name of file : ") # Demo.txt

    if(os.path.exists(fileName)):    
       fobj=open(fileName,"r")

       print(fobj.name)
       print(fobj.mode)
       print(fobj.closed)

       fobj.close()
       print(fobj.closed)

    else:
        print("There is no such file.")

if __name__ == "__main__":
    main()