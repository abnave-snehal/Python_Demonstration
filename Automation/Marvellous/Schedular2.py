import time
import datetime
import schedule

def fun():
    print("Inside fun at : ",datetime.datetime.now())

def main():
    print("Inside Marvellous Automation script at : ",datetime.datetime.now())

    schedule.every(20).seconds.do(fun)

    # Problem in this code because of fun() function is not called

if __name__ == "__main__":
    main()