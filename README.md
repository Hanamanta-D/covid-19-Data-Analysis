# COVID-19 Data Analysis Project

## Project Overview
This project performs comprehensive data analysis and visualization on COVID-19 dataset from GitHub. The analysis includes data exploration, cleaning, aggregation, feature engineering, and visualization using Python libraries.

## Dataset
- **Source**: https://raw.githubusercontent.com/SR1608/Datasets/main/covid data.csv
- **Description**: Global COVID-19 statistics including cases, deaths, GDP per capita, and human development index by location and date

## Project Objectives

### 1. Data Import & Exploration
- Import dataset using Pandas from the provided URL
- Understand dataset structure (rows, columns, data types)
- Generate statistical summaries

### 2. Data Understanding
- **High-Level Analysis**:
  - Dataset shape and dimensions
  - Column data types
  - Data statistics and descriptions

- **Low-Level Analysis**:
  - Count of unique locations
  - Continent with maximum frequency
  - Maximum and mean values in total cases
  - Quartile distribution of total deaths
  - Continent with highest human development index
  - Continent with lowest GDP per capita

### 3. Data Cleaning
- Remove duplicate observations
- Identify missing values across all columns
- Remove records with missing continent data
- Fill remaining missing values with 0

### 4. Data Transformation
- Convert date column to datetime format
- Extract month from date column
- Aggregate data by continent (maximum values)
- Create feature: total_deaths_to_total_cases ratio

### 5. Data Visualization
- Histogram with KDE for GDP per capita distribution
- Scatter plot: Total Cases vs GDP Per Capita
- Pairplot for multivariate relationship analysis
- Bar plot: Total Cases per Continent

### 6. Output
- Save processed dataframe to CSV file (df_groupby_analysis.csv)

## Technologies Used
- **Python 3.14**
- **Pandas**: Data manipulation and analysis
- **Seaborn**: Statistical data visualization
- **Matplotlib**: Plotting library

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Run the Analysis
```bash
python covid.py
```

The script will:
1. Download and load the COVID-19 dataset
2. Perform comprehensive data analysis
3. Display analysis results in console
4. Generate visualization plots
5. Save processed data to `df_groupby_analysis.csv`

## Output Files
- **df_groupby_analysis.csv**: Processed dataframe with aggregated data by continent

## Project Structure
```
COVID Data Analysis/
├── covid.py                    # Main analysis script
├── covid-data.csv              # Local copy (optional)
├── df_groupby_analysis.csv     # Output file
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Key Findings
The analysis provides insights into:
- COVID-19 case distribution across continents
- Correlation between economic development (GDP) and case numbers
- Mortality statistics by continent
- Human development index relationship with pandemic impact

## Notes
- Visualizations are displayed using matplotlib's interactive backend
- Missing values in numeric columns (except continent) are filled with 0
- Data is aggregated at the continent level using maximum values
- Date format is automatically detected and converted

## Author
Internship Project - iStudio

## Date
April 2026
