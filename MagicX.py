# Dunder method / Magic method / Special method

class demo:
    def __init__(self,a):
        self.no=a

    def __add__(self,other):
        return self.no + other.no
    
    def __sub__(self,other):
        return self.no - other.no
    
    def __mul__(self,other):
        return self.no * other.no
    
    def __truediv__(self,other):
        return self.no / other.no


obj1=demo(11)
obj2=demo(21)

print(11+21)        #32

print(obj1 + obj2)  # __add__(obj1,obj2)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 / obj2)