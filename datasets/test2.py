import pandas as pd

# Specify the file path
file_path = "/workspaces/zillow-rent-vs-buy/datasets/orlando_fl_data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Select all rows and the first 6 columns
df_six_columns = df.iloc[:, :6]

# Display the selected data
print(df_six_columns)