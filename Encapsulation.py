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
    
obj1=Arithmatic(11,10)  # Arithematic
obj2=Arithmatic(21,20)

ret=obj1.Addition()

print("Addition is : ",ret)

ret=obj2.Subtraction()
print("Subtraction is : ",ret)