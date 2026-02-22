# Steps for machine learning application:

# Step 1: Data Gathering/ Data Collection
# Step 2: Data Analysis
# Step 3: Data Cleaning
# Step 4: Model Selection
# Step 5: Model Training(Gharche exam)
# Step 6: Model testing / Evaluation
# Step 7: Model Improvment(Radio example tuning)
# Step 8: Predication / Deployment 

from sklearn import tree

#One Hot Method
#Rough:1
#Smooth:0

#Tennis:1
#Cricket:2

def main():
    print("Ball Classification Case Study:")

    #Original encoded dataset
    #Independent variables
    X=[[35,"1"],[47,"1"],[90,"0"],[48,"1"],[90,"0"],[35,"1"],
              [92,"0"],[35,"1"],[35,"1"],[35,"1"],[96,"0"],[43,"1"],
              [110,"0"],[35,"1"],[95,"0"]]
    
    #Depdent variable
    Y=["1","1","2","1","2","1","2","1","1","1","2","1","2","1","2"]


    #Indepdent variables for training
    Xtrain=[[35,"1"],[47,"1"],[90,"0"],[48,"1"],[90,"0"],[35,"1"],
              [92,"0"],[35,"1"],[35,"1"],[35,"1"],[96,"0"],[43,"1"],
              [110,"0"]]

   #Indepdent variables for testing
    Xtest=[[35,"1"],[95,"0"]]

   #Dependent variables for training
    Ytrain=[1,1,2,1,2,1,2,1,1,1,2,1,2]

   #Depdent variables for testing
    Ytest=[1,2]

    
    #tree he module ch naav ahe decisiontreeclassifier haa class ahe
    modelobj=tree.DecisionTreeClassifier()

    trainedmodel=modelobj.fit(Xtrain,Ytrain)

    result=trainedmodel.predict(Xtest)

    print("Model predicts the object as : ",result)   # 1 2

if __name__ == "__main__":
    main()