import pandas as pd

import matplotlib.pylab as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
)

border="_"*40
###################################################################
# Step 1: Load the dataset
###################################################################

print(border)
print("Step 1: Load the dataset")
print(border)

datasetPath="iris.csv"
dataFrame=pd.read_csv(datasetPath)

print("Dataset gets loaded successfully...")
print("Initial entries from dataset:")
print(dataFrame.head())

###################################################################
# Step 2: Data Analysis (EDA)
###################################################################

print(border)
print("Step 2: Data Analysis")
print(border)

print("Shape of dataset : ",dataFrame.shape)  #pandas property shape
print("Column name : ",list(dataFrame.columns))

print("Missing values (Per Column) : ")
print(dataFrame.isnull().sum())

print("Class distribution (Species count)")
print(dataFrame["species"].value_counts())

print("Stastical Report Of Dataset : ")
print(dataFrame.describe())


###################################################################
# Step 3: Decide Independent & Dependent Variables
###################################################################

print(border)
print("Step 3: Decide Independent & Dependent Variables")
print(border)

# X : Independent variables/ Features
# Y : Depdendent variables / Labels

features_cols=[
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X=dataFrame[features_cols]
Y=dataFrame["species"]

print("X shape : ",X.shape)
print("Y Shape : ",Y.shape)

###################################################################
# Step 4: Visualisation of  dataset
###################################################################

print(border)
print("Step 4: Visualisation dataset")
print(border)

# Scatter Plot
plt.figure(figsize=(7,5))

for sp in dataFrame["species"].unique():
    temp=dataFrame[dataFrame["species"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label=sp)

plt.title("Iris : Petal length Vs Petal width ")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True)
plt.show()

