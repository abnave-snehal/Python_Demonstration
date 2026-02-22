from sklearn.datasets import load_iris

def main():
    border="_"*50
    print(border)
    print("Irs Case Study:")
    print(border)

    dataSet=load_iris()

    for i in range(len(dataSet.target)):
        print("ID %d,Features %s,Label %s" %(i,dataSet.data[i],dataSet.target[i]))

    print(border)

if __name__ == "__main__":
    main()