def Add(arr):
    sum=0

    for i in range(len(arr)):
        sum=sum + arr[i]
    return sum

def main():
    size=0
    value=0
    Ret=0
    print("Enter the number of element : ")
    size=int(input())

    data=list()
    print("Enter the elements : ")
    for i in range(size):
        value=int(input())
        data.append(value)

    
    Ret=Add(data)
    print("Addition is : ",Ret)
    
if __name__ == "__main__":
    main()