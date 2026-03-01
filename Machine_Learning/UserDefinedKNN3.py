#  [A,B,C,D]
# X[1,2,3,5]
# Y[2,3,1,6]
#  [R,R,B,B]
# Predicted(3,3) -> ?

import numpy as np
import math

def EucDistance(p1,p2):
    ans=math.sqrt((p1['X']-p2['X']) ** 2 + (p1['Y']-p2['Y']) ** 2)
    return ans


def MarvellousKNeighborClassifer():
    border="_"*40

    data=[
            {'point':'A','X':1,'Y':2,'label':'Red'},
            {'point':'B','X':2,'Y':3,'label':'Red'},
            {'point':'C','X':3,'Y':1,'label':'Blue'},
            {'point':'D','X':5,'Y':6,'label':'Blue'}
        ]
    
    print(border)
    print("------ Marvellous UserDefined KNN ------")
    print(border)

    print(border)
    print("Training Data Set")
    print(border)

    for i in data:
        print(i)
    
    print(border)

    new_point={'X':3,'Y':3}

    # calculate all distances
    for d in data:
        d['distance']=EucDistance(d,new_point)

    print(border)
    print("Calcualted distances are : ")
    print(border)

    for d in data:
        print(d)

def main():

    MarvellousKNeighborClassifer()

if __name__ == "__main__":
    main()