class demo:
    no=10

    def __init__(self,A,B):   # Parametrize constrcutor
        self.value1= A
        self.value2= B

print("Class variable No : ",demo.no)   # call using class demo

obj1=demo(11,21)
obj2=demo(51,101)

# print(obj1.no)   Allowed to call using object

print("Instance variable of obj1 : ",obj1.value1,obj1.value2)       # 11 21
print("Instance variable of obj2 : ",obj2.value1,obj2.value2)       # 51 101

obj1.value1=15

demo.no=0
 
print("Instance variable of obj1 : ",obj1.value1,obj1.value2)       # 15 21
print("Instance variable of obj2 : ",obj2.value1,obj2.value2)       # 51 101

print(obj1.no)          # 0
print(obj2.no)          # 0