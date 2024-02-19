import pandas as pd

# Read the CSV file
df = pd.read_csv('/workspaces/zillow-rent-vs-buy/datasets/orlando2_fl_data.csv')

# Add a new column with "Buy" as the first row and "Rent" as the second row
df['BYvsRen'] = ["Buy", "Rent"] + [""] * (len(df) - 2)

# Save the DataFrame as a new CSV file
df.to_csv('/workspaces/zillow-rent-vs-buy/datasets/orlando_3_fl_data.csv', index=False)

# Display the DataFrame
print(df)

