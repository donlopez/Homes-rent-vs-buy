import os
import pandas as pd

# Specify the directory path
dir_path = "/workspaces/zillow-rent-vs-buy/datasets/"

# Get a list of all files in the directory
files = os.listdir(dir_path)

# Create a list to store all filtered dataframes
dfs = []

# Iterate over the list of files
for file in files:
    # Check if the file is a CSV file
    if file.endswith('.csv'):
        # Construct the full file path
        file_path = os.path.join(dir_path, file)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Filter the DataFrame
        df_filtered = df[df['RegionName'] == 'Orlando, FL']
        
        # Append the filtered DataFrame to the list
        dfs.append(df_filtered)

# Concatenate all dataframes in the list
df_all_filtered = pd.concat(dfs)

# Specify the path where the new CSV file will be saved
new_file_path = "/workspaces/zillow-rent-vs-buy/datasets/orlando_fl_data.csv"

# Create a new CSV file
df_all_filtered.to_csv(new_file_path, index=False)