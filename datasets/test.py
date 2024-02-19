import pandas as pd

# Specify the file path
file_path = "/workspaces/zillow-rent-vs-buy/datasets/orlando2_fl_data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame
print(df)