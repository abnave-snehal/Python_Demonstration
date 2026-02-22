class Parent():
    def __init__(self):
        print("Inside parent constructor : ")
        self.no1=10
        self.no2=20

    def fun(self):
        print("Inside fun method of parent : ")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside child constructor : ")
        self.a=11
        self.b=21

    def sun(self):
        print("Inside sun mehtod of child : ")

cobj=Child()