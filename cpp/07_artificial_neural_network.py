from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (confusion_matrix, accuracy_score, recall_score,
                             f1_score, roc_auc_score)
import matplotlib.pyplot as plt

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = make_pipeline(StandardScaler(),
                      MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=1000, random_state=42))
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

plt.plot(model[-1].loss_curve_)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Neural Network - Training Loss")
plt.show()
