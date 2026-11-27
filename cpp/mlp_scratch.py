from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

X = iris.data.tolist()
y = iris.target.tolist()

# Normalize dataset
for j in range(4):
    minimum = min(row[j] for row in X)
    maximum = max(row[j] for row in X)

    for i in range(len(X)):
        X[i][j] = (X[i][j] - minimum) / (maximum - minimum)

# One hot encoding
Y = []

for value in y:
    if value == 0:
        Y.append([1, 0, 0])
    elif value == 1:
        Y.append([0, 1, 0])
    else:
        Y.append([0, 0, 1])

# Initialize weights and biases
input_size = 4
hidden_size = 5
output_size = 3

w1 = [[0.1 for j in range(hidden_size)] for i in range(input_size)]
b1 = [0.1] * hidden_size

w2 = [[0.1 for j in range(output_size)] for i in range(hidden_size)]
b2 = [0.1] * output_size


# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + 2.71828**(-x))


# Training
learning_rate = 0.1
epochs = 1000

for epoch in range(epochs):

    for n in range(len(X)):

        # Forward propagation
        hidden = []

        for j in range(hidden_size):
            total = b1[j]

            for i in range(input_size):
                total += X[n][i] * w1[i][j]

            hidden.append(sigmoid(total))

        output = []

        for j in range(output_size):
            total = b2[j]

            for i in range(hidden_size):
                total += hidden[i] * w2[i][j]

            output.append(sigmoid(total))

        # Backpropagation
        output_delta = []

        for j in range(output_size):
            error = Y[n][j] - output[j]
            delta = error * output[j] * (1 - output[j])
            output_delta.append(delta)

        hidden_delta = []

        for i in range(hidden_size):
            error = 0

            for j in range(output_size):
                error += output_delta[j] * w2[i][j]

            delta = error * hidden[i] * (1 - hidden[i])
            hidden_delta.append(delta)

        # Update output weights
        for i in range(hidden_size):
            for j in range(output_size):
                w2[i][j] += learning_rate * output_delta[j] * hidden[i]

        for j in range(output_size):
            b2[j] += learning_rate * output_delta[j]

        # Update input weights
        for i in range(input_size):
            for j in range(hidden_size):
                w1[i][j] += learning_rate * hidden_delta[j] * X[n][i]

        for j in range(hidden_size):
            b1[j] += learning_rate * hidden_delta[j]

# Testing
correct = 0

for n in range(len(X)):

    hidden = []

    for j in range(hidden_size):
        total = b1[j]

        for i in range(input_size):
            total += X[n][i] * w1[i][j]

        hidden.append(sigmoid(total))

    output = []

    for j in range(output_size):
        total = b2[j]

        for i in range(hidden_size):
            total += hidden[i] * w2[i][j]

        output.append(sigmoid(total))

    prediction = output.index(max(output))

    if prediction == y[n]:
        correct += 1

accuracy = (correct / len(X)) * 100

print("Accuracy:", accuracy, "%")