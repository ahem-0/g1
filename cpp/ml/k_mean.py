from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score

X, _ = load_iris(return_X_y=True)

model = KMeans(n_clusters=3, n_init="auto", random_state=42)
clusters = model.fit_predict(X)

print("Cluster Assignments (first 15):", clusters[:15])
print(f"Silhouette Score: {silhouette_score(X, clusters):.4f}")
