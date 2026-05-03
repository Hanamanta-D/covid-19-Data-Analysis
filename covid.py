"""
COVID-19 Data Analysis Project
Author: iStudio Internship Program
Date: April 2026

This script performs comprehensive analysis on COVID-19 dataset including:
- Data import and exploration
- Data cleaning and preprocessing
- Aggregation and feature engineering
- Statistical analysis and visualization
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ===== STEP 1: IMPORT THE DATASET =====
# Source: https://raw.githubusercontent.com/SR1608/Datasets/main/covid data.csv
url = "https://raw.githubusercontent.com/SR1608/Datasets/main/covid data.csv"
print("Loading COVID-19 dataset...")
df = pd.read_csv(url)
print("Dataset loaded successfully!\n")

# ===== STEP 2: HIGH LEVEL DATA UNDERSTANDING =====
# Understanding dataset structure, dimensions, and data types
print(f"Number of rows & columns: {df.shape}")
print("\nData types of columns:")
print(df.dtypes)
print("\nInfo of dataframe:")
df.info()
print("\nDescribe of data:")
print(df.describe())

# ===== STEP 3: LOW LEVEL DATA UNDERSTANDING =====
# Detailed analysis of specific columns and metrics
# a. Unique values in location
print(f"Unique locations: {df['location'].nunique()}")

# b. Continent with maximum frequency
print(f"Continent with max frequency: {df['continent'].value_counts().idxmax()}")

# c. Maximum & mean value in 'total_cases'
print(f"Max total_cases: {df['total_cases'].max()}")
print(f"Mean total_cases: {df['total_cases'].mean()}")

# d. 25%, 50% & 75% quartile value in 'total_deaths'
print("Quartiles for total_deaths:")
print(df['total_deaths'].quantile([0.25, 0.5, 0.75]))

# e. Continent with maximum 'human_development_index'
max_hdi_idx = df['human_development_index'].idxmax()
print(f"Continent with max HDI: {df.loc[max_hdi_idx, 'continent']}")

# f. Continent with minimum 'gdp_per_capita'
min_gdp_idx = df['gdp_per_capita'].idxmin()
print(f"Continent with min GDP per capita: {df.loc[min_gdp_idx, 'continent']}")

# ===== STEP 4: FILTER DATAFRAME =====
# Selecting relevant columns for analysis
columns_to_keep = ['continent', 'location', 'date', 'total_cases', 'total_deaths', 'gdp_per_capita', 'human_development_index']
df = df[columns_to_keep]
print("Dataframe filtered with selected columns.\n")

# ===== STEP 5: DATA CLEANING =====
# a. Remove duplicates
df = df.drop_duplicates()

# b. Find missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# c. Remove observations where continent is missing
df = df.dropna(subset=['continent'])

# d. Fill missing values with 0
df = df.fillna(0)

# 6. Date time format
# a. Convert date column
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# b. Extract month
df['month'] = df['date'].dt.month

# 7. Data Aggregation
# a. Find max value using groupby on continent
df_groupby = df.groupby('continent').max().reset_index()
# b. Store the result (df_groupby is now our primary dataframe)

# 8. Feature Engineering
# a. Create 'total_deaths_to_total_cases' ratio
df_groupby['total_deaths_to_total_cases'] = df_groupby['total_deaths'] / df_groupby['total_cases']

# 9. Data Visualization
print("\n--- 9. Generating Plots ---")

# a. Univariate analysis on 'gdp_per_capita'
plt.figure(figsize=(10, 6))
sns.histplot(df_groupby['gdp_per_capita'], kde=True)
plt.title('GDP Per Capita Distribution (by Continent Max)')
plt.show()

# b. Scatter plot of 'total_cases' & 'gdp_per_capita'
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_groupby, x='gdp_per_capita', y='total_cases', hue='continent', s=100)
plt.title('Total Cases vs GDP Per Capita')
plt.show()

# c. Pairplot
sns.pairplot(df_groupby)
plt.show()

# d. Bar plot of 'continent' column with 'total_cases'
sns.catplot(data=df_groupby, x='continent', y='total_cases', kind='bar', aspect=1.5)
plt.title('Total Cases per Continent')
plt.show()

# ===== STEP 10: SAVE RESULTS =====
# Exporting processed dataframe to CSV
df_groupby.to_csv('df_groupby_analysis.csv', index=False)
print("\n" + "="*60)
print("ANALYSIS COMPLETE")
print("="*60)
print("Results saved to 'df_groupby_analysis.csv'")
print("All visualizations have been displayed.")
print("="*60)