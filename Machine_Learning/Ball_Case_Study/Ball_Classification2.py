# Steps for machine learning application:

# Step 1: Data Gathering/ Data Collection
# Step 2: Data Analysis
# Step 3: Data Cleaning
# Step 4: Model Selection
# Step 5: Model Training(Gharche exam)
# Step 6: Model testing / Evaluation
# Step 7: Model Improvment(Radio example tuning)
# Step 8: Predication / Deployment 

import sklearn

#One Hot Method
#Rough:1
#Smooth:0

#Tennis:1
#Cricket:2

def main():
    print("Ball Classification Case Study:")

    #Feature encoding
    features=[[35,"1"],[47,"1"],[90,"0"],[48,"1"],[90,"0"],[35,"1"],
              [92,"0"],[35,"1"],[35,"1"],[35,"1"],[96,"0"],[43,"1"],
              [110,"0"],[35,"1"],[95,"0"]]
    
    #Label decoding
    labels=[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

if __name__ == "__main__":
    main()

# Data set size=15(Records)