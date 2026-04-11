import matplotlib.pyplot as plt
import numpy as np

def relu(z):
    return max(0,z)

def neuron_forward(input,weight,bias):
    print("\n------Neuron Calculation Start------\n")

    print("Input (x) : ",input)
    print("Weight (w) : ",weight)
    print("Bias (b) : ",bias)

    z=sum(w * x for w,x in zip(weight,input)) + bias

    print("\n Step 1 : Weighted Sum Calculation")
    print("z=w.x+b=",z)


    y_hat=relu(z)

    print("\n Step 2 : Activation function applied")
    print("Activation function ReLU")
    print("Output (y) : ",y_hat)

    print("\n------Neuron Calculation end------")

    return z,y_hat

def plot_relu():
    z_values=np.linspace(-10,10,200)

    relu_values=np.maximum(0,z_values)

    plt.figure(figsize=(8,5))
    plt.plot(z_values,relu_values,label="ReLU Function",linewidth=2,color="green")

    plt.axhline(y=0,color="black",linewidth=0.5)
    plt.axvline(x=0,color="gray",linestyle="--")

    plt.title("ReLU Activation Function",fontsize=16)
    plt.xlabel("Input (z)",fontsize=14)
    plt.ylabel("Output",fontsize=14)

    plt.grid(True,linestyle="--",alpha=0.6)
    plt.legend()

    plt.show()


def main():
    print("\n========== Neuron Demo ==========\n")

    inputs=[1.0,2.0,3.0]

    weights=[0.6,0.4,-0.2]

    bias=0.5

    z,y_hat=neuron_forward(inputs,weights,bias)

    plot_relu()

if __name__ == "__main__":
    main()
