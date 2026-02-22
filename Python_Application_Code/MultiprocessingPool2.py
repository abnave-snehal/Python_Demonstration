
def sumCube(no):
    sum=0

    for i in range(1,no+1):
        sum = sum + (i**3)  #i**3 == (i*i*i)

    return sum   

def main():
    ret=sumCube(10)

    print(ret)

if __name__ == "__main__":
    main()