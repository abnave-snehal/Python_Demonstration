from functools import reduce 

checkEven = lambda no : no % 2 == 0

Increment = lambda no : no + 1

Add = lambda a,b : a+b

def filterX(Task,Elements):
    Result=list()

    for no in Elements:
        ret=Task(no)

        if(ret==True):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result=list()

    for no in Elements:
        Ret=Task(no)
        print("Ret data",Ret)
        Result.append(Ret)

    return Result

def main():
    data=[11,10,15,20,22,27,30]
    print("Actual data is : ",data)

    Fdata=list(filterX(checkEven,data))
    print("Data after filter is :",Fdata)

    Mdata=list(mapX(Increment,Fdata))
    print("Data after map is : ",Mdata)

    Rdata=reduce(Add,Mdata)
    print("Data after reduce is : ",Rdata)

if __name__ == "__main__":
    main()