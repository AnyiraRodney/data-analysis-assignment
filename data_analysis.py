import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Step 1: Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("Dataset loaded successfully!\n")

# Step 2: Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Step 3: Check data types and missing values
print("Dataset info:")
print(df.info(), "\n")
print("Missing values in each column:")
print(df.isnull().sum(), "\n")

# Step 4: Fill missing values (none in Iris, but included for example)
df.fillna(df.mean(), inplace=True)

# Step 5: Basic statistics
print("Basic statistics of numerical columns:")
print(df.describe(), "\n")

# Step 6: Group by species
print("Average sepal length per species:")
print(df.groupby('species')['sepal length (cm)'].mean(), "\n")

# Step 7: Data Visualizations

# Line chart of sepal length (trend by index)
plt.plot(df['sepal length (cm)'])
plt.title("Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.tight_layout()
plt.show()

# Bar chart: average sepal length per species
sns.barplot(x='species', y='sepal length (cm)', data=df)
plt.title("Average Sepal Length per Species")
plt.tight_layout()
plt.show()

# Histogram of petal length
plt.hist(df['petal length (cm)'], bins=10, color='skyblue')
plt.title("Petal Length Distribution")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter plot: sepal vs petal length
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c='orange')
plt.title("Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# Step 8: Observations
print("Observations:")
print("1. Sepal length is generally longest in the species 'virginica'.")
print("2. Petal length distribution shows clear separation between species.")
print("3. Sepal and petal lengths are positively correlated.")
