class Parent():
    def __init__(self):
        print("Inside parent constructor : ")
        self.no1=10
        self.no2=20

    def fun(self):
        print("Inside fun method of parent : ",self.no1,self.no2)

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside child constructor : ")
        self.a=11
        self.b=21

    def sun(self):
        print("Inside sun mehtod of child : ",self.a,self.b,self.no1,self.no2)

cobj=Child()

print(cobj.no1)     # 10
print(cobj.no2)     # 20

print(cobj.a)       # 11
print(cobj.b)       # 21

cobj.fun()
cobj.sun()