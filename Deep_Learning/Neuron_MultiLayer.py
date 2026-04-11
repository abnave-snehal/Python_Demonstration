import math

# ---------------------------------------------------------
# Activation Functions
# ---------------------------------------------------------

def relu(x):
    return max(0, x)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# ---------------------------------------------------------
# Utility Functions
# ---------------------------------------------------------

def calculate_weighted_sum(inputs, weights, bias):
    return sum(w * i for w, i in zip(weights, inputs)) + bias


def display_multiplication(inputs, weights):
    for i in range(len(inputs)):
        print(f"    ({weights[i]} * {inputs[i]}) = {weights[i] * inputs[i]:.3f}")


# ---------------------------------------------------------
# Hidden Layer
# ---------------------------------------------------------

def process_hidden_layer(inputs, hidden_weights, hidden_biases):
    outputs = []

    print("\n=========== HIDDEN LAYER ===========\n")

    for i in range(len(hidden_weights)):
        print(f"Hidden Neuron {i+1}:")

        weights = hidden_weights[i]
        bias = hidden_biases[i]

        print("  Step 1: Multiplication")
        display_multiplication(inputs, weights)

        z = calculate_weighted_sum(inputs, weights, bias)
        print(f"  Step 2: Add bias ({bias}) → z = {z:.3f}")

        a = relu(z)
        print(f"  Step 3: ReLU({z:.3f}) = {a:.3f}\n")

        outputs.append(a)

    return outputs


# ---------------------------------------------------------
# Output Layer
# ---------------------------------------------------------

def process_output_layer(hidden_outputs, output_weights, output_bias):
    print("\n=========== OUTPUT LAYER ===========\n")

    print("Output Neuron:")
    print("  Step 1: Multiplication")

    for i in range(len(hidden_outputs)):
        print(f"    ({output_weights[i]} * {hidden_outputs[i]:.3f}) = {output_weights[i] * hidden_outputs[i]:.3f}")

    z = calculate_weighted_sum(hidden_outputs, output_weights, output_bias)
    print(f"  Step 2: Add bias ({output_bias}) → z = {z:.3f}")

    y = sigmoid(z)
    print(f"  Step 3: Sigmoid({z:.3f}) = {y:.3f}")

    return z, y


# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------

def display_summary(hidden_outputs, final_output):
    print("\n=========== FINAL SUMMARY ===========\n")
    print("Hidden Outputs :", hidden_outputs)
    print("Final Output   :", round(final_output, 3))
    print("Confidence     :", round(final_output * 100, 2), "%")

    if final_output >= 0.5:
        print("Prediction     : Positive Class")
    else:
        print("Prediction     : Negative Class")


# ---------------------------------------------------------
# Forward Pass
# ---------------------------------------------------------

def ann_forward_pass(inputs):
    print("\n=========== INPUT LAYER ===========\n")
    print(f"Input x1 = {inputs[0]}")
    print(f"Input x2 = {inputs[1]}")

    # Hidden layer (2 neurons)
    hidden_weights = [
        [0.5, -0.2],
        [0.8, 0.4]
    ]
    hidden_biases = [0.1, -0.1]

    # Output layer (1 neuron)
    output_weights = [1.0, -1.5]
    output_bias = 0.2

    hidden_outputs = process_hidden_layer(inputs, hidden_weights, hidden_biases)

    z, final_output = process_output_layer(
        hidden_outputs,
        output_weights,
        output_bias
    )

    display_summary(hidden_outputs, final_output)


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():
    inputs = [2.0, 3.0]  # change values to test
    ann_forward_pass(inputs)


if __name__ == "__main__":
    main()