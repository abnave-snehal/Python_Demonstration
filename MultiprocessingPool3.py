import time
import os

def sumCube(no):
    print("Process is running with PID : ",os.getpid())
    sum=0

    for i in range(1,no+1):
        sum = sum + (i**3)  #i**3 == (i*i*i)

    return sum   

def main():
    data=[1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
    result=[]

    start_time=time.time()

    for i in range(0,len(data)):
        ret= sumCube(data[i])
        result.append(ret)

    end_time=time.time()

    print(result)

    print("Total execution time is : ",end_time - start_time)

if __name__ == "__main__":
    main()