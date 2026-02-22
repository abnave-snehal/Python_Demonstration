def Display(a,b,c,d):
    print(a,b,c,d)


def main():
    # Display(10,20)                Not allowed  (less parameters)
    # Display(10,20,30,40,50)       Not allowed  (extra parameters)
    Display(10,20,30,40)            #Allowed

if __name__== "__main__":
    main()