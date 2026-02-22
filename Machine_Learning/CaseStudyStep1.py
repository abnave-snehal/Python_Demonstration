import pandas as pd

import matplotlib.pylab as pld

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

