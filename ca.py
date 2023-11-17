import json
import pandas as pd
import csv
from IPython.display import display

with open('RTB.json', 'r') as file:
    data = json.load(file)
for key, value in data.items():
    print(f"{key}: {value}")

dataset = data.get('dataset', {})

# Extracting relevant information
dimension = dataset.get('dimension', {})
values = dataset.get('value', [])

# Extracting information for specific labels
labels_of_interest = ['Number of Bedrooms', 'Property Type', 'Location']
label_data = {label: dimension.get(label, {}).get('category', {}).get('label', {}) for label in labels_of_interest}

# Creating DataFrames
df_values = pd.DataFrame({'Values': values})
df_labels = pd.DataFrame(label_data)

# Merging DataFrames
df = pd.concat([df_values, df_labels], axis=1)

# Displaying the DataFrame
display(df)


#Attempt two

dataset = data.get('dataset', {})

# Extracting relevant information
dimension = dataset.get('dimension', {})
values = dataset.get('value', [])
number_of_bedrooms_data = dimension.get('C02970V03592', {}).get('category', {}).get('label', {}).values()

# Ensure that 'values' and 'number_of_bedrooms_data' have the same length
min_length = min(len(values), len(number_of_bedrooms_data))
values = values[:min_length]
number_of_bedrooms_data = list(number_of_bedrooms_data)[:min_length]

df_values = pd.DataFrame({'Value': values, 'Number of Bedrooms': number_of_bedrooms_data})

display(df_values)



try:
    # Use 'with' statement to ensure the file is properly closed after
    with open('RTB.csv', 'r', newline='') as file:
        # Create a CSV reader object using DictReader to interpret rows as dictionaries with column names as keys
        reader = csv.DictReader(file)
        # Read the CSV data into a list of dictionaries and store it in 'irish_weather_data'
        RTB_data = list(reader)
        
#Exception handling for when the file is not found or DirectoryError and raise an exception
except FileNotFoundError:
    print("Error: File not found. Please provide a valid file path.")
except IsADirectoryError:
    print("Error: The provided path points to a directory, not a file.")
print(RTB_data[0].keys())










# Creating a new JSON file 
try:
    with open('RTB.csv', 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        RTB_data = list(reader)
    json_file = 'RTB.json'
    with open(json_file, 'w') as json_output:
        json.dump(RTB_data, json_output, indent=2)
    print(f'Successfully converted CSV to JSON. Output file: {json_file}')
except FileNotFoundError:
    print("Error: File not found. Please provide a valid file path.")
except IsADirectoryError:
    print("Error: The provided path points to a directory, not a file.")
