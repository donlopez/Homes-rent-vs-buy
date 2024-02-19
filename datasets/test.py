import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('/workspaces/zillow-rent-vs-buy/datasets/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')

# Perform analysis on df1...
column_name = 'price'  # Replace 'price' with the actual column name you want to analyze
mean_value = df1[column_name].mean()
median_value = df1[column_name].median()

print(f"Mean {column_name}: {mean_value}")
print(f"Median {column_name}: {median_value}")


# Read the second CSV file
df2 = pd.read_csv('/workspaces/zillow-rent-vs-buy/datasets/Rentals_zori_uc_sfrcondomfr_sm_month.csv')


# Continue with your analysis using the data from both files

# Perform analysis on df2...
column_name = 'rent'  # Replace 'rent' with the actual column name you want to analyze
mean_value = df2[column_name].mean()
median_value = df2[column_name].median()

print(f"Mean {column_name}: {mean_value}")
print(f"Median {column_name}: {median_value}")

