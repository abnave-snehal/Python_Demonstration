import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
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
# Step 4: Create boosting model.(AdaBoost)
#-----------------------------------------------------------

boost_model=AdaBoostClassifier(
    random_state=42,
    n_estimators=50,
    learning_rate=1.0 # Weight on wrong result
    )

#-----------------------------------------------------------
# Step 5: Train boosting model.
#-----------------------------------------------------------

boost_model.fit(X_train,Y_train)

#-----------------------------------------------------------
# Step 6: Test boosting model.
#-----------------------------------------------------------

Y_pred=boost_model.predict(X_test)

#-----------------------------------------------------------
# Step 7: Evaluate the boosting model.
#-----------------------------------------------------------

print("Boosting accuracy : ",accuracy_score(Y_test,Y_pred))

print("Confusion matrix : ")
print(confusion_matrix(Y_test,Y_pred))

