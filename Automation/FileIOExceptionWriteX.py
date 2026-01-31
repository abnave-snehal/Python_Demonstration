def main():
    try:
        fobj=open("Hello.txt","w")   # File object created
        print("File gets successfully opened.")

        fobj.write("Jay Ganesh...")

    except FileNotFoundError:
        print("Unable to open file as there is no such file.")

    finally:  # finally is Optional 
        print("End of application")

if __name__ == "__main__":
    main()