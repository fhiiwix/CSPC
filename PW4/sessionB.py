import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

os.makedirs("results", exist_ok=True)

wine = load_wine(as_frame=True)
X = wine.data
cultivar = wine.target

# Scaled PCA & Scree plot
scaler = StandardScaler()
Z = scaler.fit_transform(X)

pca_scaled = PCA()
pca_scaled.fit(Z)
ratios = pca_scaled.explained_variance_ratio_
cum_ratios = np.cumsum(ratios)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(range(1, len(ratios) + 1), ratios, alpha=0.7, label="Individual")
ax.step(range(1, len(cum_ratios) + 1), cum_ratios, where="mid", label="Cumulative", color="red")
ax.axhline(0.9, color="black", linestyle="--", label="90% Variance")
ax.set_xlabel("Principal Components")
ax.set_ylabel("Explained Variance Ratio")
ax.set_title("PCA Scree Plot (Scaled Data)")
ax.legend()
plt.tight_layout()
plt.savefig("results/scree_plot.png", dpi=300)
plt.close()

# K-Means (k=3)
km3 = KMeans(n_clusters=3, init="k-means++", n_init=10, random_state=0)
km3.fit(Z)
ct = pd.crosstab(cultivar, km3.labels_)
agreement = ct.max(axis=0).sum() / len(cultivar)

agreement_df = pd.DataFrame([{
    "method": "Scaled Data", "agreement": agreement
}])
agreement_df.to_csv("results/B_agreement.csv", index=False)
print(f"Saved results/B_agreement.csv with agreement: {agreement:.4f}")