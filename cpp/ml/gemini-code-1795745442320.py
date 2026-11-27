from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split

X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

# 1. Train/Test Split Evaluation
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Test MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"Test R2:  {r2_score(y_test, y_pred):.4f}")

# 2. 5-Fold Cross-Validation
cv_mse = -cross_val_score(
    LinearRegression(), X, y, cv=5, scoring="neg_mean_squared_error"
).mean()
cv_r2 = cross_val_score(LinearRegression(), X, y, cv=5, scoring="r2").mean()

print(f"5-Fold CV MSE: {cv_mse:.4f}")
print(f"5-Fold CV R2:  {cv_r2:.4f}")