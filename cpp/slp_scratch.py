from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data.tolist()
y = iris.target.tolist()

# first 100 rows of setosa and versicolor
X = X[:100]
y = y[:100]

# split
X_train, y_train, X_test, y_test = [], [], [], []
for i in range(len(X)):
    if i % 5 == 0:
        X_test.append(X[i])
        y_test.append(y[i])
    else:
        X_train.append(X[i])
        y_train.append(y[i])

# starting weights and bias
w = [0, 0, 0, 0]
b = 0
lr = 0.1
epochs = 10


def step(z):
    if z >= 0:
        return 1
    else:
        return 0


def predict(x):
    z = b
    for i in range(4):
        z = z + w[i] * x[i]
    return step(z)


# training
for epoch in range(epochs):
    for n in range(len(X_train)):
        x = X_train[n]
        error = y_train[n] - predict(x)

        for i in range(4):
            w[i] = w[i] + lr * error * x[i]

        b = b + lr * error
    print("epoch", epoch + 1,
          "weights:", [round(v, 2) for v in w],
          "bias:", round(b, 2))

# testing
correct = 0
for n in range(len(X_test)):
    if predict(X_test[n]) == y_test[n]:
        correct = correct + 1

print("Test accuracy:", correct / len(X_test) * 100, "%")