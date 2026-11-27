from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso, Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "Lasso": Lasso(alpha=0.1),
    "Ridge": Ridge(alpha=1.0),
}

for name, model in models.items():
    # 1. Train/Test Split Evaluation
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # 2. 5-Fold Cross-Validation
    cv_mse = -cross_val_score(
        model, X, y, cv=5, scoring="neg_mean_squared_error"
    ).mean()
    cv_r2 = cross_val_score(model, X, y, cv=5, scoring="r2").mean()

    print(f"--- {name} Regression ---")
    print(f"Test MSE: {mse:.4f} | Test R2: {r2:.4f}")
    print(f"CV MSE:   {cv_mse:.4f} | CV R2:   {cv_r2:.4f}")
