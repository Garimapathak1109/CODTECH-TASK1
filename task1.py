#!/usr/bin/env python
# coding: utf-8

# In[73]:


# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[74]:


# Function to load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data
# Path to the dataset
file_path = "C:/Users/patha/OneDrive/Desktop/codtech/dataset/shopping_trends_updated.csv"
data = load_data(file_path)


# In[45]:


print(data.head())


# In[53]:


# Check data types to ensure they are numeric for correlation
print(data.dtypes) 


# In[54]:


print(data.columns)


# In[75]:


#missing value
print(data_encoded.isna().sum())


# In[76]:


# Function to display summary statistics and data info
def summarize_data(data):
    print("Data Info:")
    print(data.info())
    print("\nSummary Statistics:")
    print(data.describe())
    print("\nMissing Values:")
    print(data.isnull().sum())
# Summarize the dataset
summarize_data(data)


# In[17]:


# Function to visualize distributions
def plot_distributions(data):
    plt.figure(figsize=(16, 5))
# Age Distribution
    plt.subplot(1, 3, 1)
    sns.histplot(data['Age'], bins=15, kde=True, color='skyblue')
    plt.title('Age Distribution')
# Purchase Amount Distribution
    plt.subplot(1, 3, 2)
    sns.histplot(data['Purchase Amount (USD)'], bins=10, kde=True, color='salmon')
    plt.title('Purchase Amount Distribution')
# Review Rating Distribution
    plt.subplot(1, 3, 3)
    sns.histplot(data['Review Rating'], bins=10, kde=True, color='lightgreen')
    plt.title('Review Rating Distribution')
    plt.tight_layout()
    plt.show()
# Plot the distributions
plot_distributions(data)


# In[26]:


# Convert categorical columns to numeric
data_encoded = pd.get_dummies(data, drop_first=True)

# Handle missing values by dropping them 
data_encoded = data_encoded.dropna()


# In[42]:


# Function to plot the correlation heatmap
def plot_correlation_heatmap(data):
    plt.figure(figsize=(12, 8))  # Adjust the size for better visibility
    corr_matrix = data.corr()
 # Create the heatmap with enhanced visualization
    sns.heatmap(corr_matrix, 
                annot=True,              # Show correlation values
                annot_kws={"size": 10},  # Adjust the size of the annotations
                cmap='coolwarm',         # Use a visually appealing color palette
                linewidths=0.5,          # Add lines between cells for clarity
                linecolor='white',       # Line color between cells
                cbar_kws={"shrink": 0.75},  # Shrink color bar to fit the plot
                vmin=-1, vmax=1)         # Set the range of values for the color scale
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.yticks(rotation=0)               # Keep y-axis labels horizontal
    plt.title('Correlation Heatmap of Shopping Trends', fontsize=16, pad=20)  # Add title with padding
    plt.tight_layout()  # Adjust layout to fit everything nicely
    plt.show()
# Plot the correlation heatmap using the encoded data
plot_correlation_heatmap(data_encoded)


# In[34]:


# Function to plot box plots to detect outliers
def plot_box_plots(data):
    plt.figure(figsize=(16, 5))
# Age Box Plot
    plt.subplot(1, 3, 1)
    sns.boxplot(x=data['Age'], color='skyblue')
    plt.title('Age Box Plot')
# Purchase Amount Box Plot
    plt.subplot(1, 3, 2)
    sns.boxplot(x=data['Purchase Amount (USD)'], color='salmon')
    plt.title('Purchase Amount Box Plot')
# Review Rating Box Plot
    plt.subplot(1, 3, 3)
    sns.boxplot(x=data['Review Rating'], color='lightgreen')
    plt.title('Review Rating Box Plot')
    plt.tight_layout()
    plt.show()

# Plot the box plots
plot_box_plots(data)


# In[69]:


print(data.columns.tolist())
data.columns = data.columns.str.strip()
# Rename columns to match the scatter plot function
data.rename(columns={
    'A': 'Age',
    'B': 'Previous Purchases',
    'C': 'Purchase Amount (USD)'
}, inplace=True)


# In[70]:


print(data[['Age', 'Purchase Amount (USD)', 'Previous Purchases']].head())


# In[71]:


data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
data['Purchase Amount (USD)'] = pd.to_numeric(data['Purchase Amount (USD)'], errors='coerce')
data['Previous Purchases'] = pd.to_numeric(data['Previous Purchases'], errors='coerce')
# Check the updated data types
print(data.dtypes)


# In[72]:


# Function to plot scatter plots
def plot_scatter_plots(data):
    plt.figure(figsize=(14, 6))
# Plot Age vs Purchase Amount
    plt.subplot(1, 2, 1)
    sns.scatterplot(x='Age', y='Purchase Amount (USD)', data=data, color='orange')
    plt.title('Age vs Purchase Amount')
    plt.xlabel('Age')
    plt.ylabel('Purchase Amount (USD)')
# Plot Previous Purchases vs Purchase Amount
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='Previous Purchases', y='Purchase Amount (USD)', data=data, color='blue')
    plt.title('Previous Purchases vs Purchase Amount')
    plt.xlabel('Previous Purchases')
    plt.ylabel('Purchase Amount (USD)')
    plt.tight_layout()
    plt.show()
# Plot the scatter plots
plot_scatter_plots(data)


# # CONCLUSION
# 
# - Data Loading and Preprocessing: 
# The dataset is cleaned by handling missing values and encoding categorical variables.
# - Summary Statistics: 
# The code reviews data types, generates summary statistics, and identifies missing data points.
#   
# ### Visualizations:
# 
# - Histograms: 
# Display the distributions of Age, Purchase Amount, and Review Rating.
# - Box Plots: 
# Highlight potential outliers in Age, Purchase Amount, and Review Rating.
# - Scatter Plots: 
# Explore relationships between Age vs Purchase Amount and Previous Purchases vs Purchase Amount.
# 
# ### Key Findings:
# 
# - Skewed Distributions:
# Purchase amounts are right-skewed, indicating that most customers make lower-value purchases, with a few high-value outliers.
# - Outliers: 
# The box plots show the presence of outliers in age and purchase amounts.
# - Weak Correlation:
# Scatter plots reveal weak correlations between age and purchase amount, as well as between previous purchases and spending behavior.
