# Accept: Multiples Parameter
# Return: One value

def Marvellous1(value1,value2):
    print("Inside Marvellous1 : ",value1,value2)
    return 11


def main():
    Result= None
    Result=Marvellous1("Python",21)
    print("Return Value is:",Result)

if __name__=="__main__":
    main()