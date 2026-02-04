def main():
    try:
        fobj=open("Hello.txt","r")   # file read
        print("File gets successfully opened.")

        print("Current offset is : ",fobj.tell())

        Data=fobj.read(6)

        print("Data from file is : ",Data)

        print("Current offset is : ",fobj.tell())
        
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file.")

    finally:  # finally is Optional 
        print("End of application")

if __name__ == "__main__":
    main()