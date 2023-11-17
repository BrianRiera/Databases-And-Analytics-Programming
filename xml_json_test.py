import xml.etree.cElementTree as ET
data = '''<person>
<name>Chuck</name>
<phone type="intl">+1 734 303 4456</phone>
<email hide="yes"/>
</person>'''
tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attribute: ', tree.find('email').get('hide'))

# Define the path to the XML file and create a full file path.
path_to_file = r'C:\Users\User\Documents\GitHub\Databases-And-Analytics-Programming'
xml_File = path_to_file + r'\people.xml'

# Parse the XML file using ElementTree and create an ElementTree object.
tree = ET.parse(xml_File)

# Define the path to the CSV file and open it in write mode.
csvFile = path_to_file + r'\ResidentData.csv'
Resident_data = open(csvFile, 'w')

# Create a CSV writer object to write data to the CSV file.
csvwriter = csv.writer(Resident_data)

# Initialize an empty list to store CSV header (column names).
resident_head = []

# Initialize a counter for iterating through XML elements.
count = 0

# Loop through 'Resident' elements in the XML file.
for member in tree.findall('Resident'):
    resident = []  # Create a list to store data for each resident.
    address_list = []  # Create a list to store address details for each resident.

    # If it's the first iteration, extract column names from XML tags.
    if count == 0:
        # Extract column names from XML tags and add them to the header list.
        name = member.find('Name').tag
        resident_head.append(name)
        PhoneNumber = member.find('PhoneNumber').tag
        resident_head.append(PhoneNumber)
        EmailAddress = member.find('EmailAddress').tag
        resident_head.append(EmailAddress)
        Address = member[3].tag  # Assuming Address is the fourth child element of 'Resident'.
        resident_head.append(Address)
        
        # Write the header to the CSV file.
        csvwriter.writerow(resident_head)
        count = count + 1  # Increment the count to skip this block in the next iterations.

    # Extract data from XML elements and store them in lists.
    name = member.find('Name').text
    resident.append(name)
    PhoneNumber = member.find('PhoneNumber').text
    resident.append(PhoneNumber)
    EmailAddress = member.find('EmailAddress').text
    resident.append(EmailAddress)
    Address = member[3][0].text
    address_list.append(Address)
    City = member[3][1].text
    address_list.append(City)
    StateCode = member[3][2].text
    address_list.append(StateCode)
    PostalCode = member[3][3].text
    address_list.append(PostalCode)

    # Add the address list to the resident's data list.
    resident.append(address_list)

    # Write the resident's data to the CSV file.
    csvwriter.writerow(resident)

# Close the CSV file after writing data.
Resident_data.close()

#Exploring it 
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
    
'''<Resident Id="100">
<Name>Sample Name</Name>
<PhoneNumber>12345642357891</PhoneNumber>  ----------------------Prints this line, the first resident and second line of info
<EmailAddress>sample_name@example.com</EmailAddress>'''
print(root[0][1].text)


json.load(f) #Load JSON data from file (or file-like object)
json.loads(s) # Load JSON data from string
json.dump(j, f) # Write JSON object to file (or file like object)
json.dumps(j) # Output JSON object as string

# using XML to dict
# Import the xmltodict module for parsing XML data into a Python dictionary
import xmltodict

# Open the XML file in read mode
with open('people.xml', 'r') as file:
    # Read the XML content from the file
    xml_content = file.read()
    
    # Parse the XML content into a Python dictionary using xmltodict
    obj = xmltodict.parse(xml_content)

# Convert the Python dictionary to a JSON-formatted string using the json module
json_string = json.dumps(obj, indent=4)

# Open a new JSON file in write mode
with open('output.json', 'w') as json_file:
    # Write the JSON-formatted string to the JSON file
    json_file.write(json_string)

# The XML data from 'people.xml' has been successfully converted to 'output.json'

import xml.etree.ElementTree as ET
import json
import csv
tree = ET.parse('people.xml')
root = tree.getroot()

data_list = []
for resident in root.findall('Resident'):
    person_data = {
        'name': resident.find('Name').text,
        'PhoneNumber': resident.find('PhoneNumber').text,
        'EmailAddress': resident.find('EmailAddress').text,
    }

    address_element = resident.find('Address')
    if address_element is not None:
        person_data['StreetLine1'] = address_element.find('StreetLine1').text
        person_data['City'] = address_element.find('City').text
        person_data['StateCode'] = address_element.find('StateCode').text
        person_data['PostalCode'] = address_element.find('PostalCode').text
    else:
        person_data['StreetLine1'] = None
        person_data['City'] = None
        person_data['StateCode'] = None
        person_data['PostalCode'] = None

    data_list.append(person_data)
    
person_data
data_list

with open('people.json', 'w') as jsonfile:
    json.dump(data_list, jsonfile, indent=4)

#writing it to CSV
with open('people.csv', 'w', newline='') as csvfile:
    fieldnames = ['name','PhoneNumber','EmailAddress', 'StreetLine1', 'City', 'StateCode','PostalCode']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_list)




#Last Year CA
'''The Northwind data set, provided in XML format on Moodle, includes details of employees, customers,
products and sales for a fictitious company.
(a) Create a function to import this XML file. This function must include appropriate exception
handling clauses covering all possible error conditions and should return the parsed contents of the
XML file. [15 marks]
'''
# Import necessary modules
import xml.etree.ElementTree as ET  
import csv 

# Function to load XML file and handle exceptions
def load_file(path):
    try:
        # Open and parse the XML file
        with open(path, 'r') as file:
            tree = ET.parse(file)  # Parse the XML data into an ElementTree object
            root = tree.getroot()  # Get the root element of the XML tree
            return root  # Return the root element for further 
#Without returning the root element, the parsed XML data would be trapped within the scope of the load_file function 
#and inaccessible to the rest of your program. This returned root element can then be used by the calling code to access
#and manipulate the XML data, as demonstrated in the subsequent sections of your code.
    except FileNotFoundError:
        print(f'The file {path} was not found')  
    except IsADirectoryError:
        print(f'{path} is a directory error')    
    except PermissionError:
        print(f'Insufficient permissions to open {path}') 
    except ET.ParseError as e:
        print(f'Error parsing XML: {e}')        

# Load XML data using the load_file function
xml_root = load_file('NorthWind.xml')

# Access and print specific elements from 'Products' section
products = list(xml_root.findall('Products')[0])
for i in range(len(products)):
    if i in [0, 2, 4, 6]:
        print("********************* Product Record: ", i + 1, '***************')
        print('ProductName: ' + products[i].find('ProductName').text)  
        print('UnitsInStock: ' + products[i].find('UnitsInStock').text)  
        print('UnitsOnOrder: ' + products[i].find('UnitsOnOrder').text)  

# Print tags and text of all elements in the XML tree
if xml_root is not None:
    for element in xml_root:
        print(f'Tag: {element.tag}, Text: {element.text}')  # Print the tag and text of each element

# Access and filter customer data based on 'Country' field
customer_list = list(xml_root.findall('Customers')[0])
data_list = []  # Initialize an empty list to store filtered customer data
for customer in customer_list:
    if customer.find('Country').text == 'France':  # Check if the 'Country' field is 'France'
        name = customer.find('CompanyName').text  
        contact = customer.find('ContactName').text  
        title = customer.find('ContactTitle').text  
        phone = customer.find('Phone').text  
        _id = customer.get('CustomerID') 
        data_list.append({'_id': _id, 'name': name, 'contact': contact, 'title': title, 'phone': phone})
        # Append a dictionary representing customer data to the data_list

# Write filtered customer data to a CSV file
with open('NorthWind.csv', 'w', newline='') as csvfile:
    fieldnames = ['_id', 'name', 'contact', 'title', 'phone']  # Define CSV header field names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # Create a CSV DictWriter object
    writer.writeheader()  # Write CSV header row
    writer.writerows(data_list)  # Write customer data to the CSV file






'''There are 1,000 records in total. You have been provided with an XML file containing this 
data.
a) Create a function to import this XML file. Your function should include exception 
handling clauses. '''

try:
    with open(r'C:\Users\User\Downloads\theoDataset.xml', 'r') as file:
        tree = ET.parse(file)
        root = tree.getroot()
except FileNotFoundError:
    print('File not found')  
except IsADirectoryError:
    print('Directory error')    
except PermissionError:
    print('Insufficient permissions to open') 
except ET.ParseError as e:
    print('Error parsing XML: {e}') 
    

''') Use the print function to display the id, weight and conc values of the first, third, 
fifth, seventh, ninth and eleventh records in the XML dataset. (Hint: you may use the 
range() function). '''
index_list = [0,2,4,6,8,10]

for index in index_list:
    record = root[index]
    id = record.find('id').text
    weight = record.find('weight').text
    conc = record.find('conc').text
    print(f'Record {index +1}: id:{id}, weight:{weight}, conc:{conc}')

''' Extract the XML data and write it to a CSV file. Your file should also contain the 
column names'''

import csv


subject_list = []  # Initialize an empty list to store filtered subject data
print(subject_list)

# Iterate through each <subject> element and extract data
for subject in root.findall('subject'):
    id = subject.find('id').text
    weight = subject.find('weight').text
    dose = subject.find('dose').text
    time = subject.find('time').text
    conc = subject.find('conc').text
    subject_list.append({'id': id, 'weight': weight, 'dose': dose, 'time': time, 'conc': conc})

# Write data to CSV file
with open('TheoDataset.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'weight', 'dose', 'time', 'conc']  # Define CSV header field names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # Create a CSV DictWriter object
    writer.writeheader()  # Write CSV header row
    writer.writerows(subject_list)  # Write subject data to the CSV file




'''Create a function to import this JSON data file. Your function should include 
exception handling clauses.'''
import json
import csv
def import_weather_data(file_path):
    try:
        with open(file_path, 'r') as file:
            weather_data = json.load(file)
        return weather_data
    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

weather_data = import_weather_data('DublinAirport090220.json')
    
'''b) Using a loop structure, print the 
i. temperature
ii. weatherDescription
iii. reportTime
associated with each of the hourly observations in the JSON data'''

for observation in weather_data:
    temperature = observation.get('temperature', 'N/A')
    weather_description = observation.get('weatherDescription', 'N/A')
    report_time = observation.get('reportTime', 'N/A')

    print(f'Temperature: {temperature}°C')
    print(f'Weather Description: {weather_description}')
    print(f'Report Time: {report_time}')
    print('-' * 30)
    
try:
    with open('DublinAirport090220.json', 'r') as file:
        weather_data = json.load(file)
except FileNotFoundError:
    print("Error: File not found. Please provide a valid file path.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format in the file.")
except Exception as e:
    print(f"An error occurred: {e}")
for observation in weather_data:
    temperature = observation.get('temperature', 'N/A')
    weather_description = observation.get('weatherDescription', 'N/A')
    report_time = observation.get('reportTime', 'N/A')

    print(f'Temperature: {temperature}°C')
    print(f'Weather Description: {weather_description}')
    print(f'Report Time: {report_time}')
    print('-' * 30)
    
'''c) Extract the JSON data and write it to a CSV file. Your file should also contain the 
column names.'''

# Write to CSV
csv_file_name = 'weather_data.csv'
fieldnames = ['Temperature','Symbol','Weather Description', 'text', 'windSpeed', 'windGust', 'cardinalWindDirection', 'windDirection', 'humidity', 'rainfall', 'pressure', 'dayName', 'date','Report Time']

with open(csv_file_name, 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    for observation in weather_data:
        temperature = observation.get('temperature')
        weather_description = observation.get('weatherDescription')
        text = observation.get('text')
        windSpeed = observation.get('windSpeed')
        windGust = observation.get('windGust')
        cardinalWindDirection = observation.get('cardinalWindDirection')
        humidity = observation.get('humidity')
        rainfall = observation.get('rainfall')
        pressure = observation.get('pressure')
        dayName = observation.get('dayName')
        date = observation.get('date')
        report_time = observation.get('reportTime')
        csv_writer.writerow({'Temperature': temperature, 'Weather Description': weather_description, 'text':text, 'windSpeed':windSpeed, 'windGust':windGust,
                             'cardinalWindDirection':cardinalWindDirection,'humidity':humidity, 'rainfall':rainfall,'pressure':pressure, 'dayName':dayName, 'date':date, 'Report Time':report_time })
        

import csv
import json
import numpy
import re


'''Question 1:
The provided dataset contains hourly weather data from 25 stations across 15 counties
in Ireland for the first half of 2020. This data has been obtained from Met Eireann’s
website.
Write Python code to:
- import the provided .csv file,
- print all the column headers,
.'''
import csv
try:
    with open('irish_weather.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        irish_weather_data = list(reader)
except FileNotFoundError:
    print("Error: File not found. Please provide a valid file path.")

#print all the column headers,
print(irish_weather_data[0].keys())
        
#print the list of all counties
#print the list of all stations,
counties = []
stations = []

for row in irish_weather_data:
    county = row['county']
    station = row['station']
    if county not in counties:
        counties.append(county)
    if station not in stations:
        stations.append(station)
    
print(counties)
print(stations)


# determine the number of records where the column wdsp is not null,
#Your code should include exception handling.'''

count = 0
# Loop through irish_weather_data to count non-null 'wdsp' records
for row in irish_weather_data:
    if row.get('wdsp') is not None and row['wdsp'] != '':
        count = count + 1
print(f'The number of records in wdsp that are not null is {count}')

#Write code to determine the average temperature in Westmeath in May 2020
# Filter records for May 2020 in Westmeath and calculate average temperature

# Filter records for May 2020 in Westmeath using list comprehension
# Filter records for May 2020 in Westmeath and calculate average temperature
# Initialize variables
# Initialize variables
total_temperature = 0
count = 0

# Iterate through the data and calculate total temperature and count of valid records for May (month '05')
for row in irish_weather_data:
    date = row.get('date')
    if date and date[3:5] == '05' and row.get('county') == 'Westmeath':
        temperature = row.get('temperature')
        if temperature is not None:
            total_temperature = total_temperature + float(temperature)
            count = count + 1
            


# Calculate average temperature
average_temperature = total_temperature / count if count > 0 else 0

# Print the average temperature
print(f"The average temperature in Westmeath in May 2020 was: {average_temperature:.2f}°C")







import json
donegal_weather_data = []

# Iterate through irish_weather_data to filter records for Donegal
for row in irish_weather_data:
    if row.get('county') == 'Donegal':
        donegal_weather_data.append(row)

# Save the filtered data to donegal_weather.json
with open('donegal_weather.json', 'w') as json_file:
    json.dump(donegal_weather_data, json_file, indent=4)
    
    
    
import re

# Given IP address with leading zeros
ip_address = "216.08.094.196"

# Use re.sub() to remove leading zeros from the IP address
formatted_ip_address = re.sub(r'\b0+(\d+)\b', r'\1', ip_address)

# Print the formatted IP address
print(formatted_ip_address)




import re

import re

'''Write a Python program that uses regular expression to identify all the email address in
the text, and while keeping the username, replaces the domain with ncirl.ie'''
text = 'An email has been sent by alice@gmail.com to bob@hotmail.com regarding DAP'

# Regular expression pattern to match email addresses and replace domain with 'ncirl.ie'
formatted_text = re.sub(r'\b([\w.-]+)@([\w.-]+)\b', r'\1@ncirl.ie', text)
print(formatted_text)


'''Write a regular function that highlights the occurrence of any of the strings Python,
Regular, and Expressions'''
# Given text
text = "Regular Expressions are a powerful language for matching text patterns in Python. The re module handles regular expressions in Python. A Regular Expression can be used to find all matches in a string or simply test if a match exists. Regular Expressions help you to quickly collect some items from large piles of data just by defining some grammar rules."

# List of strings to be highlighted
words = ['Python', 'Regular', 'Expressions']

# Iterate through the list of words and highlight them in the text using regular expressions
for word in words:
    text = re.sub(r'\b' + word + r'\b', word + '**', text)

# Print the formatted text
print(text)


'''Create a 3x3 NumPy matrix with values ranging from 2 to 10. Then replace all even
numbers in the matrix with 0.
[10 marks]
Expected final result:'''

import numpy as np

# Create a 3x3 NumPy matrix with values ranging from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)

# Replace even numbers in the matrix with 0
matrix[matrix % 2 == 0] = 0

# Print the final matrix
print(matrix)




import numpy as np

# Given 2D array
my_array = np.array([[4, 6], [2, 1]])

# Sort the array along the first axis (rows)
first_axis = np.sort(my_array, axis=0)

# Sort the  result along the last axis (columns)
final_array = np.sort(first_axis, axis=1)
print(first_axis)
print(final_array)




import numpy as np

# Given multi-dimensional array
array = np.array([[0, 10, 20], [21, 8, 22], [23, 5, 9]])

# Initialize empty lists to store values and indices
numbers= []
indexes = []

# Loop through the array to find values bigger than 10 and their indices
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        if array[i, j] > 10:
            numbers.append(array[i, j])  # Store values
            indexes.append([i, j])       # Store indices as lists

# Convert the indices list to a NumPy array
indexes = np.array(indexes)

# Print values bigger than 10 and their indices

print(numbers)
print(indexes)

'''
Number 0: Index [0, 0]
Number 10: Index [0, 1]
Number 20: Index [0, 2]
Number 21: Index [1, 0]
Number 8: Index [1, 1]
Number 22: Index [1, 2]
Number 23: Index [2, 0]
Number 5: Index [2, 1]
Number 9: Index [2, 2]
'''




temperatures = []

# Iterate through the data and collect temperatures for May (month '05') in Westmeath
for row in irish_weather_data:
    date = row.get('date')
    if date[3:5] == '05' and row.get('county') == 'Westmeath':
        temperature = row.get('temperature')
        if temperature is not None:
            temperatures.append(float(temperature))  # Append temperature to the list

# Calculate the total temperature and the number of records
total_temperature = sum(temperatures)
count = len(temperatures)

# Calculate the average temperature
average_temperature = total_temperature / count if count > 0 else 0

# Print the average temperature and the count of valid records
print(f"Average Temperature in Westmeath for May 2020: {average_temperature:.2f}")


import json


# Open the JSON file and load its content
with open('RTB.json', 'r') as file:
    data = json.load(file)
for key, value in data.items():
    print(f"{key}: {value}")
    
import json
import pandas as pd
from IPython.display import display


# Assuming 'data' is your JSON data
dataset = data.get('dataset', {})

# Extracting relevant information
dimension = dataset.get('dimension', {})
values = dataset.get('value', [])
number_of_bedrooms_data = dimension.get('C02970V03592', {}).get('category', {}).get('label', {}).values()

# Ensure that 'values' and 'number_of_bedrooms_data' have the same length
min_length = min(len(values), len(number_of_bedrooms_data))
values = values[:min_length]
number_of_bedrooms_data = list(number_of_bedrooms_data)[:min_length]

# Creating DataFrames
df_values = pd.DataFrame({'Value': values, 'Number of Bedrooms': number_of_bedrooms_data})

# Displaying the DataFrame
display(df_values)
print(df_values)

# Assuming 'data' is your JSON data
dataset = data.get('dataset', {})

# Extracting relevant information
dimension = dataset.get('dimension', {})
values = dataset.get('value', [])
number_of_bedrooms_data = dimension.get('C02970V03592', {}).get('category', {}).get('label', {}).values()

# Creating DataFrames
df_values = pd.DataFrame({'Value': values, 'Number of Bedrooms': number_of_bedrooms_data})

# Displaying the DataFrame
display(df_values)



# Assuming 'data' is your JSON data
dataset = data.get('dataset', {})
dimension = dataset.get('dimension', {})

# Extract the first value associated with 'C02970V03592'
number_of_bedrooms_data = dimension.get('C02970V03592', {}).get('category', {}).get('label', {})
first_value_c02970v03592 = next(iter(dimension.get('C02970V03592', {}).get('category', {}).get('label', {}).values()), None)

print(first_value_c02970v03592)






####import pandas as pd

# Assuming 'data' is your JSON data
dataset = data.get('dataset', {})

# Extracting relevant information
dimension = dataset.get('dimension', {})
labels_of_interest = ['Number of Bedrooms', 'Property Type', 'Location']
values = dataset.get('value', [])
updated = dataset.get('updated', '')

# Extracting information for each specific label
label_data = {label: dimension.get(key, {}).get('category', {}).get('label', {}) for key, label in {
    'C02970V03592': 'Number of Bedrooms',
    'C02969V03591': 'Property Type',
    'C03004V03625': 'Location'
}.items()}

# Creating DataFrames
df_values = pd.DataFrame({'Updated': updated, 'Value': values})
df_labels = pd.DataFrame(label_data)

# Merging DataFrames
df = pd.concat([df_values, df_labels], axis=1)

# Displaying the DataFrame
display(df)
