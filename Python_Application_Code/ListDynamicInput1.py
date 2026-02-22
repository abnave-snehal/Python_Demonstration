
def main():
    size=0
    value=0

    print("Enter the number of element : ")
    size=int(input())

    data=list()
    print("Enter the elements : ")
    for i in range(size):
        value=int(input())
        data.append(value)

    print(data)
    
if __name__ == "__main__":
    main()