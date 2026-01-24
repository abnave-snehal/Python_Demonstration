def Multiplication(value1,value2):
    Ans=0
    Ans=value1 * value2
    return Ans

def main():
    No1=0
    No2=0
    Result=0

    No1=int(input("Enter first number : "))
    No2=int(input("Enter second number : "))

    Result=Multiplication(No1,No2)
    print("Muliplication is:",Result)
    
# Starter    
if __name__ == "__main__":    
    main()