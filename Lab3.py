''') Using a lambda expression, complete the mul_by_num function. This function
should take an argument and return a one argument function that multiplies any
value passed to it by the original number. Its body must be one line long:
def mul_by_num(num):
 """
 Returns a function that takes one argument
 and returns num
 times that argument.
 >>> x = mul_by_num(5)
 >>> y = mul_by_num(2)
 >>> x(3)
 15
 >>> y(-4)
 -8
 """
 "*** YOUR CODE HERE ***"
 return ______
'''


def mul_by_num(num):
    return lambda x: x*num
x = mul_by_num(5)
y = mul_by_num(2)
print(x(5))


'''2) The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by
the recurrence relation:
Fn = Fn-1 + Fn-2 with seed values F0 = 0 and F1 = 1.
Write a function that takes in a number n, and gives the Fibonacci sequence. For
example,
fib(5) = [0, 1, 1, 2, 3]
(Advanced programmers: Bonus points if you can do this using a lambda function)'''

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) # fn - fn-1 + fn-2
    return fib_sequence[:n]

fibonacci(0)
fibonacci(7)


''') Write a program to get the current weather of a city given in input. You can use the
following API documentation:
https://openweathermap.org/current
Hint: The GET request should have the following string appended at the end of the
query for auth: APPID=b35975e18dc93725acb092f7272cc6b8
You should retrieve for the city:
Temperature: 12.32°C
Wind speed: 8.7 m/s
Description: moderate rain
 Weather: Rain'''
from bs4 import BeautifulSoup
import requests
url = 'https://openweathermap.org/current'
request.get(url).append

import requests

def get_weather(city_name):
    api_key = "b35975e18dc93725acb092f7272cc6b8"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"  # Using metric units for Celsius
    
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]
        wind_data = data["wind"]

        temperature = main_data["temp"]
        wind_speed = wind_data["speed"]
        description = weather_data["description"]
        weather = weather_data["main"]

        print(f"Temperature: {temperature}°C")
        print(f"Wind speed: {wind_speed} m/s")
        print(f"Description: {description.capitalize()}")
        print(f"Weather: {weather.capitalize()}")
    else:
        print("City not found or error in fetching data.")

# Example usage
city_name = input("Enter city name: ")
get_weather(city_name)

from pprint import pprint
import requests
def weather_data(query):
    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+
    '&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
    return res.json();
def print_weather(result,city):
    print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
def main():
    city=input('Enter the city:')
    print()
    try:
        query='q='+city;
        w_data=weather_data(query);
        print_weather(w_data, city)
        print()
    except Exception as e:
        print('City name not found...', e)
if __name__=='__main__':
    main()





'''4) Write a program to read the xml file people.xml and output a csv file and json file
with the same information.
Validate the Json using https://jsonlint.com/
IImport the CSV using Excel'''

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



# using XML to dict

import xmltodict
with open('people.xml', 'r') as file:
    xml_content = file.read()
    obj = xmltodict.parse(xml_content)

# Convert the Python dictionary to a JSON-formatted string
json_string = json.dumps(obj, indent=4)

# Save the JSON string to a JSON file
with open('output.json', 'w') as json_file:
    json_file.write(json_string)


import psycopg2

def manage_database():
    try:
        # Establish a connection to the PostgreSQL database on the virtual machine
        dbConnection = psycopg2.connect(user='dap',
                                        password='dap',
                                        host='192.168.56.30',  # IP address of your virtual machine
                                        port='5432',
                                        database='postgres')

        # Create a cursor object using the connection
        dbCursor = dbConnection.cursor()

        # SQL statement to grant privileges to the user 'dap' on the 'public' schema
        grantStatement = "GRANT ALL PRIVILEGES ON SCHEMA public TO dap;"

        # Execute the GRANT SQL statement
        dbCursor.execute(grantStatement)

        # Commit the transaction
        dbConnection.commit()

        print("Privileges granted successfully!")

    except (Exception, psycopg2.Error) as dbError:
        print('Error while connecting to PostgreSQL:', dbError)

    finally:
        # Close the cursor and connection
        if dbCursor:
            dbCursor.close()
        if dbConnection:
            dbConnection.close()

# Call the function to grant privileges
manage_database()







import psycopg2
try:
    dbConnection = psycopg2.connect(user='dap',
                                    password='dap',
                                    host='192.168.56.30',
                                    port='5432',
                                    database='postgres')
    dbConnection.set_isolation_level(0) #AUTOCOMMIT
    dbCursor = dbConnection.cursor()
    dbCursor.execute('CREATE DATABASE weather;')
    dbCursor.close()
except (Exception, psycopg2.Error) as dbError:
    print('Error while connecting to PostgreSQL', dbError)
finally:
    if(dbConnection):
        dbConnection.close()
    
createString = '''
CREATE TABLE weather(
date_time timestamp PRIMARY KEY,
rain numeric(5,1),
temp numeric(5,1),
wetb numeric(5,1),
dewpt numeric(5,1),
vapps numeric(5,1),
rhum numeric(5,1),
msl numeric(7,1),
wdsp integer,
wddir integer,
ww integer,
w integer,
sun numeric(5,1),
vis integer,
clht integer,
clamt integer
);
'''

    dbConnection.set_isolation_level(0) #AUTOCOMMIT
    dbCursor = dbConnection.cursor()
    dbCursor.execute(createString)
    dbCursor.close()
except (Exception, psycopg2.Error) as dbError:
    print('Error while connecting to PostgreSQL', dbError)
finally:
    if(dbConnection):
        dbConnection.close()

import csv
try:
    dbConnection = psycopg2.connect(user='dap',
                                    password='dap',
                                    host='192.168.56.30',
                                    port='5432',
                                    database='weather')
    dbConnection.set_isolation_level(0) #AUTOCOMMIT
    dbCursor = dbConnection.cursor()
    insertString = "INSERT INTO weather VALUES ('{}',"+"{},"*14+"{})"
    with open ('weather.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip the header
        for row in reader:
            dbCursor.execute(insertString.format(*row))
    dbCursor.close()
except (Exception, psycopg2.Error) as dbError:
    print('Error while connecting to PostgreSQL', dbError)
finally:
    if(dbConnection):
        dbConnection.close()
        
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
sql = """
    SELECT
    EXTRACT(MONTH FROM date_time) AS month,
    AVG(temp) as temp,
    AVG(wdsp) AS wdsp
    FROM
    weather
    GROUP BY
    month;"""
try:
    dbConnection = psycopg2.connect(
    user = "dap",
    password = "dap",
    host = "192.168.56.30",
    port = "5432",
    database = "weather")
    weather_dataframe = sqlio.read_sql_query(sql, dbConnection)
except (Exception , psycopg2.Error) as dbError :
    print ("Error:", dbError)
finally:
    if(dbConnection):
        dbConnection.close()
        
print(weather_dataframe)

import seaborn as sns
import matplotlib.pyplot as plt
sns.barplot(x="month", y="temp", data=weather_dataframe)


import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt
sql = """SELECT date(date_time) AS obs_date, MIN(temp) as temp,
        MIN(dewpt) as dewpt FROM weather GROUP BY obs_date;"""
try:
    dbConnection = psycopg2.connect(
    user = "dap",
    password = "dap",
    host = "192.168.56.30",
    port = "5432",
    database = "weather")
    weather_dataframe = sqlio.read_sql_query(sql, dbConnection)
    sns.scatterplot(x="temp", y="dewpt", data=weather_dataframe);
except (Exception , psycopg2.Error) as dbError :
    print ("Error:", dbError)
finally:
    if(dbConnection):
        dbConnection.close()
