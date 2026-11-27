from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))

# 1. Train/Test Split Evaluation
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
acc = accuracy_score(y_test, y_pred)

print(f"TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}")
print(f"Accuracy:    {acc:.4f}")
print(f"Error Rate:  {1 - acc:.4f}")
print(f"Recall:      {recall_score(y_test, y_pred):.4f}")
print(f"Specificity: {tn / (tn + fp):.4f}")
print(f"F1-Score:    {f1_score(y_test, y_pred):.4f}")
print(f"AUC:         {roc_auc_score(y_test, y_prob):.4f}")

# 2. 5-Fold Cross-Validation
cv_acc = cross_val_score(model, X, y, cv=5, scoring="accuracy").mean()
print(f"5-Fold CV Accuracy: {cv_acc:.4f}")