import gc   # Garbage Collector

class demo:
    def __init__(self):
        print("Inside constructor : ")

    def __del__(self):
        print("Inside destructor : ")

# Allocate
obj1=demo()
obj2=demo()

# Use

# Deallocate
del obj1   # del == delete obj 
del obj2

gc.collect()   #garbace collector request send

print("End of application : ")