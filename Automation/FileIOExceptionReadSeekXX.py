# seek(kuthe,kuthun)
# kuthun: 0/1/2
# 0: Starting
# 1: Current
# 2: End

def main():
    try:
        fobj=open("Hello.txt","r")   # file read
        print("File gets successfully opened.")

        print("Current offset is : ",fobj.tell())  # 0

        fobj.seek(6,1)

        print("Current offset is : ",fobj.tell())  # 11

        Data=fobj.read(6)  # Hole file will read

        print("Current offset is : ",fobj.tell())  # 17

        print("Data from file is : ",Data)
        
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file.")

    finally:  # finally is Optional 
        print("End of application")

if __name__ == "__main__":
    main()