import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

# Generate non-linear quadratic dataset (100 samples)
rng = np.random.default_rng(42)
X = np.linspace(-3, 3, 100).reshape(-1, 1)
y = 2 * X.ravel() ** 2 + 3 * X.ravel() + 5 + rng.normal(0, 2, 100)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())

# 1. Train/Test Split Evaluation
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Test MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"Test R2:  {r2_score(y_test, y_pred):.4f}")

# 2. 5-Fold Cross-Validation
cv_mse = -cross_val_score(
    model, X, y, cv=5, scoring="neg_mean_squared_error"
).mean()
cv_r2 = cross_val_score(model, X, y, cv=5, scoring="r2").mean()

print(f"5-Fold CV MSE: {cv_mse:.4f}")
print(f"5-Fold CV R2:  {cv_r2:.4f}")
