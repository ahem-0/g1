import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

X, y = load_diabetes(return_X_y=True)
X = X[:, [2]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = make_pipeline(PolynomialFeatures(degree=3), LinearRegression())
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 score:", r2_score(y_test, y_pred))
print("5-fold CV R2:", cross_val_score(model, X, y, cv=5, scoring="r2").mean())
print("5-fold CV MSE:", -cross_val_score(model, X, y, cv=5, scoring="neg_mean_squared_error").mean())

x_line = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
plt.scatter(X, y)
plt.plot(x_line, model.predict(x_line), color="red")
plt.xlabel("BMI")
plt.ylabel("Disease progression")
plt.title("Polynomial Regression (degree 3)")
plt.show()
