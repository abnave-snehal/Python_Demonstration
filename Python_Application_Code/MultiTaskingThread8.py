import threading

def display(no):
    print("Inside display : ",no)

def main():
    t=threading.Thread(target=display,args=(11,))
    t.start()
    

if __name__ == "__main__":
    main()