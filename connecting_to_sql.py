
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
try:
    dbConnection = psycopg2.connect(
                                    user='dap',
                                    password='dap',
                                    host='192.168.56.30',  # IP address of your virtual machine
                                    port='5432',
                                    database='weather')
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


######
import psycopg2
import csv

def manage_database():
    try:
        dbConnection = psycopg2.connect(
            user='dap',
            password='dap',
            host='192.168.56.30',
            port='5432',
            database='postgres'
        )
        dbCursor = dbConnection.cursor()

        grantStatement = "GRANT ALL PRIVILEGES ON SCHEMA public TO dap;"
        dbCursor.execute(grantStatement)
        dbConnection.commit()
        print("Privileges granted successfully!")

    except (Exception, psycopg2.Error) as dbError:
        print('Error while connecting to PostgreSQL:', dbError)

    finally:
        if dbCursor:
            dbCursor.close()
        if dbConnection:
            dbConnection.close()

# Call the function to grant privileges
manage_database()

try:
    dbConnection = psycopg2.connect(
        user='dap',
        password='dap',
        host='192.168.56.30',
        port='5432',
        database='postgres'
    )
    dbConnection.set_isolation_level(0)  # AUTOCOMMIT
    dbCursor = dbConnection.cursor()
    dbCursor.execute('CREATE DATABASE test;')
    dbConnection.commit()
    dbCursor.close()
except (Exception, psycopg2.Error) as dbError:
    print('Error while connecting to PostgreSQL', dbError)
finally:
    if dbConnection:
        dbConnection.close()

# Create the table in the "public" schema
createString = '''
CREATE TABLE public.weather_1 (
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

try:
    dbConnection = psycopg2.connect(
        user='dap',
        password='dap',
        host='192.168.56.30',
        port='5432',
        database='test'
    )
    dbConnection.set_isolation_level(0)  # AUTOCOMMIT
    dbCursor = dbConnection.cursor()
    dbCursor.execute(createString)
    dbConnection.commit()
    dbCursor.close()
except (Exception, psycopg2.Error) as dbError:
    print('Error while connecting to PostgreSQL', dbError)
finally:
    if dbConnection:
        dbConnection.close()

# Insert data into the "weather_1" table
try:
    dbConnection = psycopg2.connect(
        user='dap',
        password='dap',
        host='192.168.56.30',
        port='5432',
        database='test'
    )
    dbConnection.set_isolation_level(0)  # AUTOCOMMIT
    dbCursor = dbConnection.cursor()
    insertString = "INSERT INTO public.weather_1 VALUES ('{}'," + "{}," * 14 + "{})"
    
    with open('weather.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip the header
        for row in reader:
            dbCursor.execute(insertString.format(*row))
    
    dbConnection.commit()
    dbCursor.close()

except (Exception, psycopg2.Error) as dbError:
    print('Error while connecting to PostgreSQL', dbError)
finally:
    if dbConnection:
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