
# Procedural 
def checkEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False

def main():
    value=0
    Ret=False

    print("Enter number :")
    value=int(input())

    Ret=checkEven(value)

    print(Ret)

if __name__ == "__main__":
    main()