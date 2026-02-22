
# Procedural 
def checkEven(no):
    if(no % 2 == 0):
        print("It is even")
    else:
        print("It is odd")

def main():
    value=0

    print("Enter number :")
    value=int(input())

    checkEven(value)

if __name__ == "__main__":
    main()