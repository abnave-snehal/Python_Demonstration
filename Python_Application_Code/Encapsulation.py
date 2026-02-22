class Arithmatic:
    def __init__(self,a,b):         # Magic method/constructor/dunder method
        self.no1=a
        self.no2=b
        print("Object gets created successfully : ")

    def Addition(self):     # instance method Addition
        asn=0
        ans=self.no1 + self.no2
        return ans

    def Subtraction(self):     # instance method Addition
        ans=0
        ans=self.no1 - self.no2
        return ans
    
obj1=Arithmatic(11,10)  # Arithmatic(id(obj1),11,10) -> __init__(id(obj1),11,10)
obj2=Arithmatic(21,20)  # Arithmatic(id(obj2),21,20) -> __init__(id(obj2),21,20)

ret=obj1.Addition()     # Addition(id(obj1))   -> Addition(1000)
print("Addition is : ",ret)    #21

ret=obj2.Subtraction()  # Subtraction(id(obj2))    -> Subtraction(2000)
print("Subtraction is : ",ret)      # 1