from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (confusion_matrix, accuracy_score, recall_score,
                             f1_score, roc_auc_score, RocCurveDisplay)
import matplotlib.pyplot as plt

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print("TP:", tp, "TN:", tn, "FP:", fp, "FN:", fn)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Error:", 1 - accuracy_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("Specificity:", tn / (tn + fp))
print("F1-score:", f1_score(y_test, y_pred))
print("AUC:", roc_auc_score(y_test, y_prob))
print("5-fold CV accuracy:", cross_val_score(model, X, y, cv=5).mean())

RocCurveDisplay.from_estimator(model, X_test, y_test)
plt.title("Logistic Regression - ROC Curve")
plt.show()
