import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


#-----------------------------------------------------------
# Step 1: Load the dataset.
#-----------------------------------------------------------

df=pd.read_csv("breast_cancer.csv")
print("Shape of dataset : ",df.shape)
print("First 5 records : ",df.head())


#-----------------------------------------------------------
# Step 2: Separate features and labels.
#-----------------------------------------------------------

X=df.drop("target",axis=1)
Y=df["target"]

#-----------------------------------------------------------
# Step 3: Split dataset for training and testing.
#-----------------------------------------------------------

X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    random_state=42,
    test_size=0.2  # 80%
)


#-----------------------------------------------------------
# Step 4: Create base model.
#-----------------------------------------------------------

base_model=DecisionTreeClassifier(random_state=42)

#-----------------------------------------------------------
# Step 5: Create bagging model.
#-----------------------------------------------------------

bagging_model=BaggingClassifier(
    estimator=base_model, #this is individual model
    n_estimators=10,  #to create a model
    random_state=42
)


#-----------------------------------------------------------
# Step 6: Train bagging model.
#-----------------------------------------------------------


bagging_model.fit(X_train,Y_train)

#-----------------------------------------------------------
# Step 7: Test bagging model.
#-----------------------------------------------------------

Y_pred=bagging_model.predict(X_test)

#-----------------------------------------------------------
# Step 8: Evaluate the bagging model.
#-----------------------------------------------------------

print("Bagging accuracy : ",accuracy_score(Y_test,Y_pred))

print("Confusion matrix : ")
print(confusion_matrix(Y_test,Y_pred))

