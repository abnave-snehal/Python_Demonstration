import numpy as np

input=np.array([2.0,3.0,4.0])

weight=np.array([0.5,0.3,0.2])

bias=0.1

#Z=(x1*w1 + x2*w2 + x3*w3) + bias

weight_sum=np.dot(input,weight)+bias

def relu(x):
    return max(0,x)

output=relu(weight_sum)


print("Input : ",input)
print("Output : ",output)
print("Bias : ",bias)
print("Weighted Sum(Z) : ",weight_sum)
print("Final Output : ",output)