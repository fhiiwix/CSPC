import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

try:
    df_heart = pd.read_csv('Heart_disease_cleveland_new.csv')
except FileNotFoundError:
    df_heart = pd.read_csv('heart.csv')

continuous_vars = ['age', 'chol', 'trestbps', 'thalach']
print(df_heart[continuous_vars].describe())

for var in continuous_vars:
    stat, p_val = stats.shapiro(df_heart[var].dropna())
    print(f"{var}: W={stat:.4f}, p-value={p_val:.4f}")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.ravel()
for i, var in enumerate(continuous_vars):
    axes[i].hist(df_heart[var].dropna(), bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    axes[i].set_title(var)
plt.tight_layout()
plt.savefig('heart_distributions.png', dpi=300)
plt.close()

group_healthy = df_heart[df_heart['target'] == 0]['thalach']
group_disease = df_heart[df_heart['target'] == 1]['thalach']

t_stat, p_val = stats.ttest_ind(group_healthy, group_disease, equal_var=False)
print(f"T-test thalach: t={t_stat:.4f}, p={p_val:.2e}")

mean_h, sem_h = group_healthy.mean(), group_healthy.sem()
mean_d, sem_d = group_disease.mean(), group_disease.sem()

plt.figure(figsize=(6, 6))
plt.bar(['Healthy (0)', 'Disease (1)'], [mean_h, mean_d], 
        yerr=[1.96*sem_h, 1.96*sem_d], capsize=5, color=['cornflowerblue', 'salmon'], alpha=0.8)
plt.ylabel('thalach')
plt.savefig('thalach_comparison.png', dpi=300)
plt.close()

pearson_r, p_pearson = stats.pearsonr(df_heart['age'], df_heart['thalach'])
print(f"Age vs Thalach r={pearson_r:.4f}, p={p_pearson:.2e}")

plt.figure(figsize=(8, 6))
plt.scatter(df_heart['age'], df_heart['thalach'], c=df_heart['target'], cmap='Set1', alpha=0.7)
plt.xlabel('age')
plt.ylabel('thalach')
plt.savefig('age_thalach_scatter.png', dpi=300)
plt.close()

df_chem = pd.read_csv('chemicals_cancer.csv')
corr_benz, _ = stats.pearsonr(df_chem['benzene'], df_chem['malignancy'])
corr_cadm, _ = stats.pearsonr(df_chem['cadmium'], df_chem['malignancy'])
print(f"Benzene corr: {corr_benz:.4f}")
print(f"Cadmium corr: {corr_cadm:.4f}")

print("Benzene vs Pollution:", stats.pearsonr(df_chem['benzene'], df_chem['pollution_index'])[0])
print("Cadmium vs Pollution:", stats.pearsonr(df_chem['cadmium'], df_chem['pollution_index'])[0])
print("Malignancy vs Pollution:", stats.pearsonr(df_chem['malignancy'], df_chem['pollution_index'])[0])

subset = df_chem[(df_chem['pollution_index'] > 45) & (df_chem['pollution_index'] < 55)]
print(f"Stratified Benzene: {stats.pearsonr(subset['benzene'], subset['malignancy'])[0]:.4f}")
print(f"Stratified Cadmium: {stats.pearsonr(subset['cadmium'], subset['malignancy'])[0]:.4f}")

target_probs = df_heart['target'].value_counts(normalize=True)
entropy = -sum(p * np.log2(p) for p in target_probs if p > 0)
print(f"Entropy: {entropy:.4f}")