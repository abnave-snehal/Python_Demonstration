import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#--------------------------------------------------------
# Function name :PreservedModel
# Description :It is used to preserved model on secondery
# Parameters :model,filename
# Return :None
# Date :14/03/2026
# Auther :Snehal Abnave
#--------------------------------------------------------

def LoadPreserveModel(filename):
   loade_model=joblib(filename)

   print("Model successfully loaded")

 #######################################  

def PreservedModel(model,filename):
   joblib.dump(model,filename)

   print("Model preserved successfully with name : ",filename)

#--------------------------------------------------------
# Function name :TrainTitanicModel
# Description :It does split X,Y,Training data,testing data
# Parameters :df
# Return :None
# Date :14/03/2026
# Auther :Snehal Abnave
#--------------------------------------------------------

def TrainTitanicModel(df):
   #Split features and labels
   X=df.drop("Survived",axis=1)
   Y=df["Survived"]

   print("Features : ")
   print(X.head())

   print("Labels : ")
   print(Y.head())

   print("Shape of X :",X.shape)
   print("Shape of Y : ",Y.shape)

   X_train,X_test,Y_train,y_test=train_test_split(
      X,
      Y,
      test_size=0.2,
      random_state=42
   )

   print("X_train Shape : ",X_train.shape)
   print("X_test Shape : ",X_test.shape)
   print("Y_train Shape : ",Y_train.shape)
   print("Y_test Shape : ",X_test.shape)

   model=LogisticRegression(max_iter=1000)

   model.fit(X_train,Y_train)

   print("Model trained successfully")

   print("\n Intercept of model : ")
   print(model.intercept_)

   print("\nCoefficient of model") #zip is used to don columns ektra kara
   for feature,coeficient in zip(X.columns,model.coef_[0]):
      print(feature, " : ",coeficient)

   PreservedModel(model,"MarvellousTitanic.pkl")

   loaded_model=LoadPreserveModel("Marvelloistitanic.pkl")

   Y_pred-loaded_model.predit(X_test)

   accuracy=accuracy_score(Y_pred,Y_test)




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
# Function name :CleanTitanicData
# Description :It does preprocessing, 
#              It removed unnecessary columns
#              It handles missing values, 
#              It converts text data to numeric format
#              It does encoding to categorical columns
# Parameters :df -> Pandas dataframe
# Return :    df -> Clean pandas dataset 
# Date :14/03/2026
# Auther :Snehal Abnave
#--------------------------------------------------------

def CleanTitanicData(df):
   DisplayInfo("Step 2: Original Data")
   print(df.head())

   # Remove unnecessary columns
   drop_columns=["Passengerid","zero","Name","Cabin"]
   existing_columns=[col for col in drop_columns if col in df.columns]

   print("\n Columns to be droped : ")
   print(existing_columns)

   # drop unwanted columns
   df=df.drop(columns=existing_columns)


   DisplayInfo("Step 2: Data after column removed")
   print(df.head())
   

   # Handle afe columns
   if "Age" in df.columns:
      print("Age column before filling missing values")
      print(df["Age"].head(10))


      #Coerce-> Invalid value gets converted into NaN
      df["Age"]=pd.to_numeric(df["Age"],errors="coerce")

      age_median=df["Age"].median()

      #Replaced missing values with median
      df["Age"]=df["Age"].fillna(age_median)

      print("\n Age column after preprocessing :")
      print(df["Age"].head(10))

      # Handle fare column
   if "Fare" in df.columns:
      print("\n Fare column before preprocessing")
      print(df["Fare"].head(10))

      df["Fare"]=pd.to_numeric(df["Fare"],errors="coerce")

      fare_median=df["Fare"].median()

      print("\n Median of fare columns is : ",fare_median)

      #Replace missing values with median
      df["Fare"]=df["Fare"].fillna(fare_median)

      print("\n Fare column after preprocessing :")
      print(df["Fare"].head(10))

   # Handle embarked columns
   if "Embarked" in df.columns:
      print("\n Embarked column before preprocessing")
      print(df["Embarked"].head(10))

      # Convert the data into string
      df["Embarked"]=df["Embarked"].astype(str).str.strip()

      # Remove missing values
      df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)

      # Get most frequent values
      embarked_mode=df["Embarked"].mode()[0]
      print("\n Mode of embarked columns : ",embarked_mode)

      print("\n embarked columns after preprocessing :")
      print(df["Embarked"].head(10))

    # Handle sex column
   if "Sex" in df.columns:
      print("\n sex column before preprocessing")
      print(df["Sex"].head(10))

      df["Sex"]=pd.to_numeric(df["Sex"],errors="coerce")

      print("\n Sex columns after preprocessing :")
      print(df["Sex"].head(10))

   DisplayInfo("Data after preprocessing")
   print(df.head(10))

   print("\n Missing values after preprocessing")
   print(df.isnull().sum())


   # Encode Embarked column
   df=pd.get_dummies(df,columns=["Embarked"],drop_first=True)
   print("\n Data after encoding")

   print(df.head())

   print("Shape of dataset : ",df.shape)

   # convert boolean columns into integer
   for col in df.columns:
      if df[col].dtype==bool:
         df[col]=df[col].astype(int)
   
   print("\n Data after encoding")

   print(df.head())

   
   return df

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

   df=CleanTitanicData(df)

   TrainTitanicModel(df)

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