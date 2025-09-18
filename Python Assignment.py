# Load dataset
df = pd.read_csv("sample_data.csv")

# Show first 5 rows
print(df.head())

# Get basic info
print(df.info())

# Summary statistics
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Example: Average of a numeric column
print("Average:", df["column_name"].mean())

# Example: Group by a column and get mean
print(df.groupby("Category")["Sales"].mean())


# Line plot
df["column_name"].plot(kind="line", title="Line Plot Example")
plt.show()

# Histogram
df["column_name"].plot(kind="hist", bins=10, title="Histogram")
plt.show()

# Bar chart (grouped data)
df.groupby("Category")["Sales"].sum().plot(kind="bar", title="Sales by Category")
plt.show()

# Scatter plot
df.plot(kind="scatter", x="Age", y="Salary", title="Age vs Salary")
plt.show()
