import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = load_diabetes()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {"Ridge": Ridge(alpha=1.0), "Lasso": Lasso(alpha=0.5)}
coefs = {}

for name, reg in models.items():
    model = make_pipeline(StandardScaler(), reg)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    coefs[name] = reg.coef_
    print(name)
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("R2 score:", r2_score(y_test, y_pred))
    print("5-fold CV R2:", cross_val_score(model, X, y, cv=5, scoring="r2").mean())
    print("5-fold CV MSE:", -cross_val_score(model, X, y, cv=5, scoring="neg_mean_squared_error").mean())
    print()

pos = np.arange(len(data.feature_names))
plt.bar(pos - 0.2, coefs["Ridge"], width=0.4, label="Ridge")
plt.bar(pos + 0.2, coefs["Lasso"], width=0.4, label="Lasso")
plt.xticks(pos, data.feature_names)
plt.ylabel("Coefficient")
plt.title("Ridge vs Lasso Coefficients")
plt.legend()
plt.show()
