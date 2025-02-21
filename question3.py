import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 1. Load and Filter Dataset
# ==============================
df = pd.read_csv('data/wms-management-survey/clean/wms_da_textbook.csv')

# Filter out Mexico and keep only firms with 100-5000 emp_firm
df = df[(df['country'] == 'United States') & (df['emp_firm'].between(100, 5000))]

# ==============================
# 2. Summary Statistics
# ==============================
# Management Score Summary
management_stats = df['management'].describe()[['mean', '50%', 'std']]
management_stats.index = ['Mean', 'Median', 'Std Dev']
print("\nManagement Score Summary:")
print(management_stats)

# Firm Size Summary
firm_size_stats = df['emp_firm'].describe()[['mean', '50%', 'std']]
firm_size_stats.index = ['Mean', 'Median', 'Std Dev']
print("\nFirm Size Summary:")
print(firm_size_stats)

# ==============================
# 3. Visualizations - Histograms
# ==============================
# Management Score Histogram
plt.figure(figsize=(7, 5))
sns.histplot(df['management'], bins=15, stat='percent', color='blue', edgecolor='black')
plt.title('Management Score Distribution')
plt.xlabel('Management Score')
plt.ylabel('Percent')
plt.savefig('results/question3_results/management_score_histogram.png')
plt.close()

# Firm Size Histogram
plt.figure(figsize=(7, 5))
sns.histplot(df['emp_firm'], bins=15, stat='percent', color='green', edgecolor='black')
plt.title('Firm Size Distribution')
plt.xlabel('Number of Employees')
plt.ylabel('Percent')
plt.savefig('results/question3_results/firm_size_histogram.png')
plt.close()

# ==============================
# 4. Conditional Probabilities by Firm Size
# ==============================
# Categorize firms into Small, Medium, and Large
bins = [0, 199, 999, 5000]
labels = ['Small', 'Medium', 'Large']
df['firm_size_category'] = pd.cut(df['emp_firm'], bins=bins, labels=labels)
df['management_rounded'] = df['management'].round(0)  # Round to nearest integer

# Calculate probabilities
conditional_probs = df.groupby(['firm_size_category', 'management_rounded'], observed=False).size().unstack().apply(lambda x: x / x.sum(), axis=1)
print("\nConditional Probabilities of Management Scores by Firm Size:")
print(conditional_probs)

# Stacked Bar Chart
conditional_probs.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.title('Conditional Probability of Management Score by Firm Size')
plt.xlabel('Firm Size')
plt.ylabel('Probability')
plt.savefig('results/question3_results/stacked_bar_chart.png')
plt.close()

# ==============================
# 5. Conditional Means
# ==============================
conditional_means = df.groupby('firm_size_category')['management'].mean()
print("\nConditional Means of Management Score by Firm Size:")
print(conditional_means)
