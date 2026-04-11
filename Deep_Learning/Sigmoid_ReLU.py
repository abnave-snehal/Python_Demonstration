import math
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# STEP 1 : Activation Functions
# ---------------------------------------------------------

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def relu(z):
    return max(0, z)


# ---------------------------------------------------------
# STEP 2 : Neuron Forward Pass
# ---------------------------------------------------------

def neuron_forward(inputs, weights, bias, activation_func):

    print("\n----- NEURON CALCULATION START -----\n")

    print("Inputs (x)   :", inputs)
    print("Weights (w)  :", weights)
    print("Bias (b)     :", bias)

    # Weighted sum
    z = sum(w * x for w, x in zip(weights, inputs)) + bias

    print("\nStep 1 : Weighted Sum")
    print("z =", z)

    # Activation
    y_hat = activation_func(z)

    print("\nStep 2 : Activation Function Applied")
    print("Activation Function :", activation_func.__name__)
    print("Output (ŷ) :", y_hat)

    print("\n----- NEURON CALCULATION END -----\n")

    return z, y_hat


# ---------------------------------------------------------
# STEP 3 : Plot Sigmoid vs ReLU
# ---------------------------------------------------------

def plot_sigmoid_relu():

    z_values = np.linspace(-10, 10, 200)

    sigmoid_values = 1 / (1 + np.exp(-z_values))
    relu_values = np.maximum(0, z_values)

    plt.figure(figsize=(8, 5))

    plt.plot(z_values, sigmoid_values, label="Sigmoid", linewidth=2)
    plt.plot(z_values, relu_values, label="ReLU", linewidth=2)

    # Reference lines
    plt.axhline(y=0)
    plt.axhline(y=1)
    plt.axvline(x=0, linestyle="--")

    plt.title("Sigmoid vs ReLU Activation Functions")
    plt.xlabel("Input (z)")
    plt.ylabel("Output")

    plt.grid(True)
    plt.legend()

    plt.show()


# ---------------------------------------------------------
# STEP 4 : Main Function
# ---------------------------------------------------------

def main():

    print("\n========= ACTIVATION FUNCTION COMPARISON =========\n")

    inputs = [1.0, 2.0, 3.0]
    weights = [0.6, 0.4, -0.2]
    bias = 0.5

    # Sigmoid
    print("=== Sigmoid Neuron ===")
    neuron_forward(inputs, weights, bias, sigmoid)

    # ReLU
    print("=== ReLU Neuron ===")
    neuron_forward(inputs, weights, bias, relu)

    # Plot graph
    plot_sigmoid_relu()


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()