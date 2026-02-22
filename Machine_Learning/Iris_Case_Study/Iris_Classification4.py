from sklearn.datasets import load_iris

def main():
    print("Irs Case Study:")

    dataSet=load_iris()

    print(dataSet.data[0])
    print(dataSet.data[1])
    print(dataSet.data[2])
    print(dataSet.data[3])  

    print(dataSet.target[0])  
    print(dataSet.target[1]) 
    print(dataSet.target[2]) 
    print(dataSet.target[3]) 

    print(dataSet.target[50])
    print(dataSet.target[51])
    print(dataSet.target[52])
    print(dataSet.target[53])

    print(dataSet.target[100])
    print(dataSet.target[101])
    print(dataSet.target[102])
    print(dataSet.target[103])

if __name__ == "__main__":
    main()