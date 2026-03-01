import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def MarvellousPredictor():
    # Load the data
    x=[1,2,3,4,5]
    y=[3,4,2,4,5]

    print("Values of Indepdndent variables :",x)
    print("Values of Dependent variables : ",y)

    mean_x=np.mean(x)
    mena_y=np.mean(y)

    print("X_MEAN is : ",mean_x)  #Xbar
    print("Y_MEAN is : ",mena_y)  #Ybar



def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()