# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
from IPython.display import display
# Define the URL of the webpage to scrape
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'

# Use a with statement to manage the request and BeautifulSoup objects
with requests.get(url) as page:
    # Raise an exception if the request was not successful
    page.raise_for_status()
    
    # Parse the HTML content
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the table with class 'wikitable sortable'
    table = soup.find('table', class_='wikitable sortable')

    # Print the table to verify if it's the correct one
    print(table)

    # Check if the table is found
    if table:
        # Find the first row within the table to extract column headers
        first_row = table.find('tr')

        # Get all column headers from the first row
        column_headers = first_row.find_all('th')

        # Extract column names
        column_names = [header.text.strip() for header in column_headers]
        print(column_names)
    else:
        print("Table not found on the webpage.")

    # Create an empty DataFrame with column names extracted from the table
    df = pd.DataFrame(columns=column_names)

    # Find all rows in the table
    column_data = table.find_all('tr')

    # Loop through rows, starting from the third row (assuming the first two rows are headers)
    for row in column_data[2:]:
        # Extract 'Rank' from the first cell (th tag)
        rank = row.find('th').text.strip()

        # Extract data from other cells (td tags)
        row_data = row.find_all('td')
        other_data = [data.text.strip() for data in row_data]

        # Insert rank at the beginning of other_data
        other_data.insert(0, rank)

        # Append the row to the DataFrame
        df.loc[len(df)] = other_data
# Display the resulting DataFrame without column truncation
with pd.option_context('display.max_columns', None):
    display(df)

# Set Pandas display options to show all columns and prevent column text truncation
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)



df.to_csv(r'C:\Users\User\OneDrive\Desktop\Python Env\Database&Analytics_Programming\Companies.csv', index = False)



#Second Page
url_2 = 'https://www.scrapethissite.com/pages/forms/'
page_1 = requests.get(url_2)
hockey_page = BeautifulSoup(page_1.text, 'html')
print(hockey_page.prettify())
hockey_page.find('p', class_ = 'lead').text.strip()
hockey_page.find('th').text.strip() # find team name


with open('index.html', 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')

print(doc.prettify())
tag = doc.title
print(tag.string)
#changing title in document
tag.string = 'hello'

#how to save changes to doc
with open('changed.html', 'w') as file:
    file.write(str(doc))


# showing first instance of p tag
tags = doc.find_all('p')[0]
# parsing the p tag for specific case 'b'
print(tags.find_all('b'))



#tech with tim video 2
#changing attribute
tag = doc.find('option')
tag['selected'] = 'false'
#adding tag
tag['color'] = 'blue'
#to see attributes
print(tag.attrs)

#looking for multiple tags
tags = doc.find_all(['p', 'div'])
#search for combination, option tag with text undergraduate if you want attribute add value = 'name'
tags = doc.find_all(['option'], text = 'Undergraduate')

'class_ to search for class'
#regular expression to find price of items
tags = doc.find_all(text=re.compile('\$.*'), limit = 1)

#how to save changes to doc
with open('changed.html', 'w') as file:
    file.write(str(doc))
    
    
    
#Navigating the HTML tree

url_3 = 'https://coinmarketcap.com/'
result_3 = requests.get(url_3).text
doc_3 = BeautifulSoup(result_3, 'html.parser')

tbody = doc_3.tbody
trs = tbody.contents
#can also use next sibling, previous sibling, plural siblings etc
print(trs[1].previous_sibling)
print(trs[0].parent.name)
print(list(trs[0].descendants)) # can also use .content, children (slightly different)
prices = {}
#just getting the currency and price from the table
for tr in trs:
    for td in tr.contents[2:4]:
        print(td)
        print()

#cleaning up the above code for just price and currency 
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    
    prices[fixed_name] = fixed_price
prices

fib = [0,1,1,2,3,5,7,13,21,34,55]
result = filter(lambda x: x%2 ==0, fib)
print(list(result))



import practice_with_numpy as np
from scipy import stats

# Sample data
sample_data = [142, 127, 171, 137, 161, 183, 148, 124]

# Calculate mean and standard deviation of the sample
mean = np.mean(sample_data)
std_dev = np.std(sample_data, ddof=1)  # ddof=1 for sample standard deviation

std_dev 
# Degrees of freedom
df = len(sample_data) - 1

# t-value for 95% confidence level and 7 degrees of freedom
t_value = stats.t.ppf(0.975, df)
t_value

# Margin of error
margin_of_error = t_value * (std_dev / np.sqrt(len(sample_data)))

# Calculate confidence interval
lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error

print("95% Confidence Interval:", (lower_bound, upper_bound))


