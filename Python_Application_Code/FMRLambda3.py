from functools import reduce

def main():
    data=[11,10,15,20,22,27,30]
    print("Actual data is : ",data)

    Fdata=list(filter((lambda no : no % 2 == 0),data))
    print("Data after filter is :",Fdata)

    Mdata=list(map((lambda no : no + 1),Fdata))
    print("Data after map is : ",Mdata)

    Rdata=reduce((lambda a,b : a+b),Mdata)
    print("Data after reduce is : ",Rdata)

if __name__ == "__main__":
    main()