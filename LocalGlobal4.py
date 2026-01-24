no=11           # Global variable

def fun():
    global no 
    print("Value of no from fun() is :",no)    # 11
    no=no+1                                    # 11+1
    print("Value of no from fun() is :",no)    # 12

print("Value of no is : ",no)                  # 11     
fun()
print("Value of no is : ",no)                  # 12  