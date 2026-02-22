from functools import reduce 

# def checkEven(no):
#     return (no % 2 == 0)

checkEven = lambda no : no % 2 == 0

# def Increment(no):
#     return no+1

Increment = lambda no : no + 1

# def Add(a,b):
#     return a+b

Add = lambda a,b : a+b
def main():
    data=[11,10,15,20,22,27,30]
    print("Actual data is : ",data)

    Fdata=list(filter(checkEven,data))
    print("Data after filter is :",Fdata)

    Mdata=list(map(Increment,Fdata))
    print("Data after map is : ",Mdata)

    Rdata=reduce(Add,Mdata)
    print("Data after reduce is : ",Rdata)

if __name__ == "__main__":
    main()