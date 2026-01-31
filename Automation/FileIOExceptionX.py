def main():
    try:
        open("Demo.txt","r")   # Default parament is r
        print("File gets successfully opened.")

    except FileNotFoundError:
        print("Unable to open file as there is no such file.")

    finally:  # finally is Optional 
        print("End of application")

if __name__ == "__main__":
    main()