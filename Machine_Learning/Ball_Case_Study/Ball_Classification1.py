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

def main():
    print("Ball Classification Case Study:")

    # Data loading / Data gathering
    features=[[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rought"],[90,"Smooth"],[35,"Rough"],
              [92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"Smooth"],[43,"Rough"],
              [110,"Smooth"],[35,"Rough"],[95,"Smooth"]]

    labels=["Tennis","Tennis","Cricket","Tennis","Circekt","Tennis","Cricket","Tennis","Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]

if __name__ == "__main__":
    main()

# Data set size=15(Records)