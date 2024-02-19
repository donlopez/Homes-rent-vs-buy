import pandas as pd

# Specify the file paths
file_path1 = "/workspaces/zillow-rent-vs-buy/datasets/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
file_path2 = "/workspaces/zillow-rent-vs-buy/datasets/Rentals_zori_uc_sfrcondomfr_sm_month.csv"

# Read the CSV files into DataFrames
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# Filter the DataFrames
orlando_df1 = df1[df1['RegionName'] == 'Orlando, FL']
orlando_df2 = df2[df2['RegionName'] == 'Orlando, FL']

# Concatenate the filtered DataFrames
orlando_df = pd.concat([orlando_df1, orlando_df2])

# Specify the output file path
output_file_path = "/workspaces/zillow-rent-vs-buy/datasets/orlando2_fl_data.csv"

# Write the new DataFrame to a new CSV file
orlando_df.to_csv(output_file_path, index=False)