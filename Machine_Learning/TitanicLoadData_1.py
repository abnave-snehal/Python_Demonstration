import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#--------------------------------------------------------
# Function name :DisplayInfo
# Description :It display the formated title
# Parameters :title(str)
# Return :None
# Date :14/03/2026
# Auther :Snehal Abnave
#--------------------------------------------------------

def DisplayInfo(title):
   print("\n"+"="*70)
   print(title)
   print("="*70)

#--------------------------------------------------------
# Function name :ShowData()
# Description:It shows basic information about the dataset.
# Parameters :df df -> Pandas dataframe object
#             message message -> Heading text to disply 
# Return :None
# Date :14/03/2026
# Auther :Snehal Abnave
#--------------------------------------------------------
def ShowData(df,message):
   DisplayInfo(message)

   print("First 5 rows of dataset")
   print(df.head())

   print("\n Shape of dataset")
   print(df.shape)

   print("\n Column names : ")
   print(df.columns.tolist())

   print("\n Missing values in each column : ")
   print(df.isnull().sum())


#--------------------------------------------------------
# Function name :MarvellousTitanicLogistic
# Description :This is main pipeline controller it loads
#              the dataset,show rows data,it preprocess
#              dataset &train the model
# Parameters :Datapath of dataset file
# Return :None
# Date :14/03/2026
# Auther :Snehal Abnave
#--------------------------------------------------------

def MarvellousTitanicLogistic(Datapath):
   DisplayInfo("Step 1: Loading the dataset")

   df=pd.read_csv(Datapath)

   ShowData(df,"Initial dataset")

#--------------------------------------------------------
# Function name :main
# Description :String point of the application
# Parameters :None
# Return :None
# Date :14/03/2026
# Auther :Snehal Abnave
#--------------------------------------------------------

def main():
 MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

    
if __name__ == "__main__":
    main()