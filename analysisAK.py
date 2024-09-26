'''from datetime import datetime, timedelta

# Get today's date
today = datetime.now()

# Print dates for the next 100 days
for i in range(100):
    cur = today - timedelta(days=i)
    s=str(cur)
    print(s.split('-'))
'''

import pandas as pd

# Load the two Excel files
file1 = 'file25.csv'
file2 = 'comb.csv'

# Read the Excel files into DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Combine the DataFrames
# This can be done using concat for stacking them vertically
combdf = pd.concat([df1, df2], ignore_index=True)

# Save the combined DataFrame to a new Excel file
comb = 'comb.csv'
combdf.to_csv(comb, index=False)
'''
print(f'Combined Excel file saved as: {combined_file}')


import requests
def download_file(url, filename):
    try:
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Write the content to a file
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded successfully: {filename}")
        else:
            print(f"Failed to download file: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")



file_url = "https://archives.nseindia.com/products/content/sec_bhavdata_full_21092024.csv"
download_file(file_url, "f11.csv")


from datetime import datetime

# Example date
date_string = '2024-09-25'  # Format: YYYY-MM-DD

# Convert the string to a datetime object
date_object = datetime.strptime(date_string, '%Y-%m-%d')

# Get the day name
day_name = date_object.strftime('%A')

print(f'The day of the week for {date_string} is {day_name}.')
'''