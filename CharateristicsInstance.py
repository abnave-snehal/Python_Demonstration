import gc   # Garbage Collector

class demo:
    # class variable
    no1= 10
    no2= 11

    def __init__(self):
        # Instance variable
        self.A=101
        self.B=201
        print("Inside constructor : ")

    def __del__(self):
        print("Inside destructor : ")

print(demo.no1)
print(demo.no2)

obj=demo()

print(obj.A)
print(obj.B)