import os

def main():
    fileName=input("Enter the name of file : ") # Demo.txt

    if(os.path.exists(fileName)):    
       fobj=open(fileName,"w")

       print(fobj.readable())
       print(fobj.writable())
       print(fobj.seekable())

    else:
        print("There is no such file.")

if __name__ == "__main__":
    main()