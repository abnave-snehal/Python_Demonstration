class demo:
    no=10

    def __init__(self,A,B):   # Parametrize constrcutor
        self.value1= A
        self.value2= B

    def fun(self):
        print("Inside instance method fun : ",self.value1,self.value2)

    @classmethod
    def sun(cls):
        print("Inside class method sun : ",cls.no)

demo.sun()   
print("Class variable no : ",demo.no)

obj=demo(11,21)

obj.fun()
print("Instance variable : ",obj.value1,obj.value2)