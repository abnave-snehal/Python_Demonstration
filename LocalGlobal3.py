no=11           # Global variable

def fun():
    no=21       # Local variable
    print("Value of no from fun() is :",no)    # 21
    no=no+1
    print("Value of no from fun() is :",no)    # 22

print("Value of no is : ",no)                  # 11     
fun()
print("Value of no is : ",no)                  # 11  