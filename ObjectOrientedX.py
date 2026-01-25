class Arithmatic:
    def Addition(self,a,b):
        return a + b

    def Subtraction(self,a,b):
        return a - b

no1=0
no2=0
ans=0

no1=int(input("Enter first number : "))
no2=int(input("Enter second number : "))

obj=Arithmatic()

ans= obj.Addition(no1,no2)
print("Addition is : ",ans)

ans= obj.Subtraction(no1,no2)
print("Subtraction is : ",ans)