def main():
    try:
        open("Hello.txt","w")   # If file is not there then it will create
        print("File gets successfully opened.")

    except FileNotFoundError:
        print("Unable to open file as there is no such file.")

    finally:  # finally is Optional 
        print("End of application")

if __name__ == "__main__":
    main()