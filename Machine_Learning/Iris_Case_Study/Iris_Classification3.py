from sklearn.datasets import load_iris


def main():
    print("Irs Case Study:")

    dataSet=load_iris()

    # Metadata of dataset
    print("Indepdendent variables are : ")
    print(dataSet.feature_names)
    print("Length of Independent variables is : ",len(dataSet.feature_names))

    print("Depdent variables are : ")
    print(dataSet.target_names)
    print("Length of Depdent variables is : ",len(dataSet.target_names))
    
if __name__ == "__main__":
    main()