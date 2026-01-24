import threading

def sumEven(no):
    sum=0

    for i in range(2,no+1,2):
        sum = sum + i
    print("The summation of even number is : ",sum)

def sumOdd(no):
    sum=0

    for i in range(1,no+1,2):
        sum = sum + i
    print("The summation of odd number is : ",sum)    

def main():
  sumEven(100000000)
  sumOdd(1000000)
    
if __name__ == "__main__":
    main()