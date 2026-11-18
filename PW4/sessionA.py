import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, confusion_matrix, precision_score, recall_score, f1_score, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

os.makedirs("results", exist_ok=True)

df = pd.read_csv("data/concrete.csv")
df = df.drop_duplicates().reset_index(drop=True)

X = df.drop(columns=["strength"])
y = df["strength"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_test = lr.predict(X_test)
print(f"Linear Regression Test RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_test)):.2f}, Test R2: {r2_score(y_test, y_pred_test):.4f}")

# Residual plot against age
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(X_test["age"], y_test - y_pred_test, alpha=0.6, color="purple")
ax.axhline(0, color="black", linestyle="--")
ax.set_xscale("log")
ax.set_xlabel("Age (log scale)")
ax.set_ylabel("Residuals (True - Pred)")
ax.set_title("Linear Regression Residuals vs Age")
plt.tight_layout()
plt.savefig("results/residuals_age.png", dpi=300)
plt.close()

# Classification (strength >= 40)
y_class = (df["strength"] >= 40).astype(int)
Xc_train, Xc_test, c_train, c_test = train_test_split(X, y_class, test_size=0.2, random_state=42, stratify=y_class)

# Chosen KNN (K=5)
chosen_knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
chosen_knn.fit(Xc_train, c_train)
knn_preds = chosen_knn.predict(Xc_test)

tn, fp, fn, tp = confusion_matrix(c_test, knn_preds).ravel()
metrics_df = pd.DataFrame([{
    "model": "KNN_K5", "TP": tp, "FP": fp, "FN": fn, "TN": tn,
    "accuracy": accuracy_score(c_test, knn_preds),
    "precision": precision_score(c_test, knn_preds, zero_division=0),
    "recall": recall_score(c_test, knn_preds, zero_division=0),
    "f1": f1_score(c_test, knn_preds, zero_division=0)
}])
metrics_df.to_csv("results/A_metrics.csv", index=False)
print("Saved results/A_metrics.csv")