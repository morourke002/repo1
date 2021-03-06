# Python Dictionary for doing common things
	# starting with pandas and common modules like os

#Data Cleaning and Preprocessing Dictionary.

# 1) Exploratory data analysis

# Univariate visualization of and summary statistics for each field in the raw dataset
# Bivariate visualization and summary statistics for assessing the relationship between each variable in the dataset and the target variable of interest (e.g. time until churn, spend)
# Multivariate visualizations to understand interactions between different fields in the data
# Dimensionality reduction to understand the fields in the data that account for the most variance between observations and allow for the processing of a reduced volume of data
# Clustering of similar observations in the dataset into differentiated groupings, which by collapsing the data into a few small data points, patterns of behavior can be more easily identified

# 2) Dealing with missing values

# Drop the columns where all elements are missing values:
df.dropna(axis=1, how='all')

# Drop the columns where any of the elements are missing values
df.dropna(axis=1, how='any')

# Keep only the rows which contain 2 missing values maximum
df.dropna(thresh=2)

# Drop the columns where any of the elements are missing values
df.dropna(axis=1, how='any')

# Fill all missing values with the mean of the particular column
df.fillna(df.mean())

# Fill any missing value in column 'A' with the column median
df['A'].fillna(df['A'].median())

# Fill any missing value in column 'Depeche' with the column mode
df['Depeche'].fillna(df['Depeche'].mode())

3) Dealing with outliers
4) Dealing with imbalance data
5) Data Transformations
	-- normalization
	-- min-max standardization
6) Finishing touches

#opening and printing a txt file.
import os
location_of_files = 'C:\\Users\\H\\Desktop\\Intermediate Python'
file_name = 'example.txt'

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())