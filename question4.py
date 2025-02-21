import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1. Load Dataset
# ==============================
df = pd.read_excel('data/Canada-population-data-2024.xlsx')  # Columns: ['Age Group', 'Men', 'Women']
df = df[df['Age Group'] != 'All ages']
# ==============================
# 2. Data Transformation (Percent of Total Males/Females)
# ==============================
total_males = df['Men'].sum()
total_females = df['Women'].sum()

df['Male_Percent'] = 0 - (df['Men'] / total_males) * 100 # Negative for left side
df['Female_Percent'] = (df['Women'] / total_females) * 100

# ==============================
# 3. Create Population Pyramid
# ==============================
plt.figure(figsize=(10, 8))

# Horizontal bars for Males (Left side, Negative Values)
plt.barh(df['Age Group'], df['Male_Percent'], color='blue', label='Men')

# Horizontal bars for Females (Right side, Positive Values)
plt.barh(df['Age Group'], df['Female_Percent'], color='pink', label='Women')

# ==============================
# 4. Styling and Labels
# ==============================
plt.title('Population Pyramid')
plt.xlabel('Percentage of Gender Population')
plt.ylabel('Age Group')
plt.axvline(0, color='black', linewidth=0.8)  # Vertical line at zero
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Labels on bars
for index, value in enumerate(df['Male_Percent']):
    plt.text(value - 0.5, index, f'{abs(value):.1f}%', ha='right', va='center', color='white')

for index, value in enumerate(df['Female_Percent']):
    plt.text(value + 0.5, index, f'{value:.1f}%', ha='left', va='center', color='white')

# Invert y-axis so youngest age group is at the bottom
plt.gca().invert_yaxis()

# Legend and Show Plot
plt.legend()
plt.tight_layout()
plt.savefig('results/question4_results/population_pyramid.png')
plt.close()
