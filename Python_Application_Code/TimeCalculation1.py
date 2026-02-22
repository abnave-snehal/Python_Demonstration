
def Factorial(no):
    fact=1
    
    for i in range(1,no+1):
        fact=fact * i
    return fact


def main():
    value=int(input("Enter the number : "))

    ret=Factorial(value)
    print("Factorial for a number is : ",ret)
    
if __name__ == "__main__":
    main()