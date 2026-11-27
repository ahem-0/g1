from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score

X, _ = load_iris(return_X_y=True)

model = AgglomerativeClustering(n_clusters=3, linkage="ward")
clusters = model.fit_predict(X)

print("Cluster Assignments (first 15):", clusters[:15])
print(f"Silhouette Score: {silhouette_score(X, clusters):.4f}")