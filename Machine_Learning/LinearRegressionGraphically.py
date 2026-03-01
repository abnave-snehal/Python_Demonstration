import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def MarvellousPredictor():
    # Load the data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    print("Values of Indepdndent variables :",X)
    print("Values of Dependent variables : ",Y)

    mean_x=np.mean(X)
    mena_y=np.mean(Y)

    print("X_MEAN is : ",mean_x)  #Xbar
    print("Y_MEAN is : ",mena_y)  #Ybar

    n=len(X)  #5

    #y=mX+C

    #m=(sum (x-X_bar) * (y-Y_bar)) / (sum (x-X_bar) ** 2)

    numerator=0
    denominator=0

    for i in range(n):
        numerator=numerator + ((X[i]- mean_x) * (Y[i] - mena_y))
        denominator=denominator + ((X[i]-mean_x) ** 2)

    m=numerator / denominator
    print("Slope of line ie m : ",m)  # 0.4

    C=mena_y - (m * mean_x)
    print("Y intercept of line C ie C : ",C)

    x=np.linspace(1,6,n)
    print(x)
    y=C + m * x

    plt.plot(x,y,color='g',label="Regression Line")
    plt.scatter(X,Y,color='r',label="Scatter Plot")

    plt.xlabel("X: Independent variables")
    plt.ylabel("Y:Dependent vairable")

    plt.legend()
    plt.show()

    # claculate R2

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()