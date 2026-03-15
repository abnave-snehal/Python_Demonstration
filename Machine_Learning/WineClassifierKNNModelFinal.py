import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border="_"*50

    # Step 1 : Load the dataset from CSV file
    print(border)
    print("Step 1: Load the dataset from CSV file")
    print(border)

    df=pd.read_csv(DataPath)

    print(border)
    print("Some entires from dataset")
    print(df.head())
    print(border)

    # Step 2: Clean the dataset by removing empty rows
    print(border)
    print("Step 2: Clean the dataset by removing empty rows")
    print(border)

    df.dropna(inplace=True)
    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])
    print(border)

    # Step 3: Separate Indepdent and Depdent Variables
    print(border)
    print("Step 3: Separate Indepdent and Depdent Variables")
    print(border)

    X=df.drop(columns=['Class'])   # remove class coloums
    Y=df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(border)
    print("Input Columns : ",X.columns.to_list())
    print("Output Column : Class")

    
    # Step 4: Split the dataset for training and testing
    print(border)
    print("Step 4: Separate Indepdent and Depdent Variables")
    print(border)

    X_train,X_test,Y_train,Y_test=train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print(border)
    print("Inforamtion of training and testing data")
    print("X_train Shap : ",X_train.shape)
    print("X_test Shap : ",X_test.shape)
    print("Y_train Shap : ",Y_train.shape)
    print("Y_test Shape : ",Y_test.shape)


    # Step 5: Feature Scaling
    print(border)
    print("Step 5: Feature Scaling")
    print(border)

    scaler=StandardScaler()
    # Indepdent variable scaling
    X_train_scaled=scaler.fit_transform(X_train)
    X_test_scaled=scaler.fit_transform(X_test)
    print("Feature scaling is done")

    # Setp 6 : Explore multiple values of K
    # Hyperparameter tuning  (K)

    accuracy_scores=[]
    K_values=range(1,21)

    for k in K_values:
        model=KNeighborsClassifier(n_neighbors=k)  #default value of k=5
        model.fit(X_train_scaled,Y_train)
        y_pred=model.predict(X_test_scaled)
        accuracy=accuracy_score(Y_test,y_pred)
        accuracy_scores.append(accuracy)

    print(border)
    print("Accuracy Report of all K values from 1 to 20")

    for value in accuracy_scores:
        print(value)
    
    print(border)

    # Step 7: Plot graph of K Vs Accuracy
    print(border)
    print("Step 7: Plot graph of K Vs Accuracy")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker='o')
    plt.title("K Value Vs Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

    # Step 8: Find best vlaue of k
    print(border)
    print("Step 8: Find best vlaue of k")
    print(border)

    best_k=list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of K is : ",best_k)

    # Step 9: Build final model using best value of k
    print(border)
    print("Step 9: Build final model using best value of k")
    print(border)

    final_model=KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled,Y_train)
    y_pred=final_model.predict(X_test_scaled)

    # Step 10: Calculate final accuracy
    print(border)
    print("Step 10: Calculate final accuracy")
    print(border)

    accuracy=accuracy_score(Y_test,y_pred)
    print("Accuracy of model is : ",accuracy*100)

    # Step 11: Display Confusion Matrix
    print(border)
    print("Step 11: Display Confusion Matrix \n")
    print(border)

    cm=confusion_matrix(Y_test,y_pred)
    print("Confusion matrix : ",cm)

    # Step 12: Display Classification report
    print(border)
    print("Step 12: Display Classification report")
    print(border)

    print(classification_report(Y_test,y_pred))

def main():
    border="_"*50
    print(border)
    print("Wine Classifier Using KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()