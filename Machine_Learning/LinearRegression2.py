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

    n=len(x)  #5

    #y=mX+C

    #m=(sum (x-X_bar) * (y-Y_bar)) / (sum (x-X_bar) ** 2)

    numerator=0
    denominator=0

    for i in range(n):
        numerator=numerator + ((x[i]- mean_x) * (y[i] - mena_y))
        denominator=denominator + ((x[i]-mean_x) ** 2)

    m=numerator / denominator
    print("Slope of line ie m : ",m)  # 0.4

    C=mena_y - (m * mean_x)
    print("Y intercept of line C ie C : ",C)




def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()