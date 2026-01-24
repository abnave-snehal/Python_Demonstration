
def checkEven(no):
    if(no % 2 == 0):
        print("It is even : ",no)
    else:
        print("It is odd : ",no)


def main():
    checkEven(21)       #Positional argument
    checkEven(no=22)    #Keyword argument

if __name__ == "__main__":
    main()
