class demo:
    no=10

    def __init__(self,A,B):   # Parametric constrcutor
        self.value1= A
        self.value2= B

print("Class variable No : ",demo.no)

obj1=demo(11,21)
obj2=demo(51,101)

print("Instance variable of obj1 : ",obj1.value1,obj1.value2)
print("Instance variable of obj2 : ",obj2.value1,obj2.value2)