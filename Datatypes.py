while True:
    user_input = input('Please enter text containing at least 5 characters: ')
    if len(user_input) >= 5:
        print('First character:', user_input[0])
        print('Third character:', user_input[2])
        print('Fifth character:', user_input[4])
        break   
    
"""Create a snippet of Python code to test if the following are equivalent to False:

An empty string ""
An empty list []
An empty set {}
An empty tuple ()
An example to test if the None type is equivalent to False is provided as a guide."""
empty_values = ["", [], set(), ()]

# Iterate through the list and test if each empty value is equivalent to False
for value in empty_values:
    if not value:
        print(f"{value} is equivalent to False")
    else:
        print(f"{value} is not equivalent to False")

a = input('please enter course title here')
b = input('please enter profession')
c = 'hello'
print(c, f'welcome {a} {b}')

my_mark = 82.15
print(f'my mark in the exam was {my_mark:3.1f}!') #the 3 stands for minimum width 3

degree = 'Bachelors in Data Analytics'
updated_degree = degree.replace('Bachelors', 'Masters')
print(updated_degree)

'''Create a short piece of Python code that prompts the user to enter a string and then prompts the user to enter a second string. 
Then test if the strings are the same and print a message to the user indicating if they are or if they are not.'''
user_input = input('Enter text here')
second_user_input = input('Enter second text here')
if user_input == second_user_input:
    print("Both words match")
else:
    print('Both words do not match')
    
'''Write some Python code that prompts the user to enter a whole number. 
You should then convert that number to an int, square it and print the result.
You can convert an int to a string using the str() typecasting function.'''
user_input = input('enter number here')
try:
    number = int(user_input)
    square = number**2
    print(f'{number} is the number selected and if we square it we get {square}')
except:
    print('Invalid selection please use a number')
    
'''Create a snippet of Python code to prompt the user to enter a temperature in Celsius. You should convert this to a float. Then you should test the value and print one of the following:

The string ‘cold’ if the temperature is less than or equal to 10.
The string ‘warm’ if the temperature is greater than 10 and less than or equal to 25.
The string ‘hot’ if the temperature is greater than 25.'''

user_input = input('Please enter temperature in celsius')
try: 
    temperature = float(user_input)
    if temperature <= 10:
        print('cold')
    elif temperature <=25:
        print('warm')
    else:
        print('hot')
except:
    print('Please enter a number')

'''4 Repetition statements
Write some Python code that repeatedly prompts 
the user to enter a string until the string entered is exactly equal to ‘exit’ (without the quotes).'''
user_input = input('please type exit here')

while user_input != 'exit':
    print('Invalid input. Please try again.')
    user_input = input('please type exit here')

print('Congratulations! You typed "exit".')

'''Create a short piece of Python code that repeated prompts the user to enter items for a shopping basket 
until the string ‘exit’ is entered (without the quotes). Each item entered should be added to a list variable
called shopping. When ‘exit’ is entered, the entire list should be printed.

'''
shopping_list = []
user_input = input('Enter shopping item here ')
while True:
    shopping_list.append(user_input)
    user_input = input('Please add another item or type exit to stop ')
    if user_input.lower() == 'exit':
        break
print('here is your shopping list: ', shopping_list)


# Python bootcamp
while True:
    user_input = input('Please enter currency in euros here: ')
    try:
        number = float(user_input)  # Use float() instead of int() to handle both integers and floats
        cent = int(number * 100)  # Convert to cents and ensure it's an integer
        print(f'You have {cent} cents')
        break  # Exit the loop if valid input is provided
    except ValueError:
        print('Invalid input. Please enter a valid number.')

a = float(input('PLease enter 1st grade here'))
b= float(input('PLease enter 2nd grade here'))
c = float(input('PLease enter 3rd grade here'))
d = float(input('PLease enter 4th grade here'))
e = float(input('PLease enter 5th grade here'))
project = float(input('PLease enter project grade here'))
total_grade = (a+b+c+d+e)*0.1 + project *0.5
if total_grade >= 40:
    print(f'Congratulations you passed with a score of {total_grade}')
else:
    print(f'Unfortunately you failed with a score of {total_grade}')

# Confidence level (e.g., 95% confidence interval)
confidence_level = 0.95

# Calculate the critical value from the t-distribution
alpha = 1 - confidence_level
degrees_of_freedom = sample_size - 1
critical_value = stats.t.ppf(1 - alpha/2, degrees_of_freedom)

# Calculate the margin of error
margin_of_error = critical_value * (std_dev / np.sqrt(sample_size))

# Calculate the confidence interval
lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error

print("Confidence Interval: [{:.2f}, {:.2f}]".format(lower_bound, upper_bound))
mean
std_dev
critical_value
lower_bound
alpha
degrees_of_freedom

# Confidence level (e.g., 99% confidence interval)
confidence_level = 0.99

# Calculate the critical value from the t-distribution
alpha = 1 - confidence_level
degrees_of_freedom = sample_size - 1
critical_value = stats.t.ppf(1 - alpha/2, degrees_of_freedom)

# Calculate the margin of error
margin_of_error = critical_value * (std_dev / np.sqrt(sample_size))

# Calculate the confidence interval
lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error

print("99% Confidence Interval: [{:.2f}, {:.2f}]".format(lower_bound, upper_bound))



# Sample data (replace this with your actual dataset)
data = np.array([20, 20, 18, 22, 25, 19, 23, 21, 24])

# Calculate mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data, ddof=1)  # ddof=1 applies Bessel's correction (n-1) for sample standard deviation
sample_size = len(data)

# Confidence level (e.g., 95% confidence interval)
confidence_level = 0.95

# Calculate the degrees of freedom
degrees_of_freedom = sample_size - 1

# Calculate the critical t-value from the t-distribution
alpha = 1 - confidence_level
critical_t_value = stats.t.ppf(1 - alpha/2, degrees_of_freedom)

# Calculate the margin of error
margin_of_error = critical_t_value * (std_dev / np.sqrt(sample_size))

# Calculate the confidence interval
lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error

print(f'95% confidence interval {lower_bound:.2f}, {upper_bound:.2f}')


a = 'brian'
print(id(a))
b = 'brian
print(id(b))
id(a) == id(b)


'''3) Create a list to store the following values: 1, 2, 3, 4, 5, 6 and assign this
list to a variable called myList .
Print the contents myList .
Print the contents of myList in reverse using index slicing.
Print the contents of myList in reverse using a loop.
Append 10 random integers to myList using a loop.
Extend myList with the following list [200, 300] .
Store the last number in the list in a variable called lastVal and remove that
value from myList . ['''
    
my_list = [ 1,2,3,4,5,6]

print(my_list)
print(my_list[::-1])
for i in reversed(my_list):
    print(i)
for i in my_list[::-1]:
    print(i)
    
import random
while len(my_list) < 17:
    random_integer = random.randint(1,100)
    my_list.append(random_integer)
    
print(my_list)
print(len(my_list))

for i in range(1,10):
    random_integer = random.randint(1,100)
    my_list.append(random_integer)
print(my_list)

my_list.extend([200,300])
print(my_list)
lastVal = my_list[-1]
my_list.remove(lastVal)
print(my_list)

'''Create an empty dictionary object called myDict . Using a loop structure, add an
entry to myDict for each value in myList . The key values for entries in myDict
should be integer values commencing at 0 .'''

my_Dict = {}
for index, value in enumerate(my_list):
    my_Dict[index] = value
    
print(my_Dict)

'''5) Write code to generate the first 6 rows of Pascal’s Triangle. [Note: Please attempt
this without accessing an algorithm specification from the web!!! For this task you
should implement the required loop controls and use appropriate data-structures.
When printing each row ensure that values are separated by a TAB character. ]
Your output should be
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
Investigate how to define functions in Python. Create a function that will print the
first n rows of Pascal’s Triangle.'''

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
# Create an instance of the Solution class
solution_instance = Solution()

# Call the generate function for 6 rows
pascals_triangle_6_rows = solution_instance.generate(6)

# Print the generated Pascal's Triangle
print(pascals_triangle_6_rows)

   
user_input = input('What does the gup say?')

while user_input != 'bork':
    user_input = input('Incorrect, try again: ')

print('Congratulations! You one smart bork')