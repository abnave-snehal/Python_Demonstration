import gc   # Garbage Collector
class demo:
    def __init__(self):
        print("Inside constructor : ")

    def __del__(self):
        print("Inside destructor : ")

# Allocate
obj=demo()

# Use

# Deallocate
del obj   # del == delete obj 

gc.collect()   #garbace collector request send

print("End of application : ")