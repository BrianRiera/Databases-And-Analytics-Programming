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

'''Write some Python code that creates an ndarray with 4 rows and 5 columns, filled with all zeros.
Set the value in the first column and 3rd row to be equal to 3. Set the value in the fourth column and second row to be equal 
to 5. Then print the contents of the ndarray'''

import numpy as np
my_array = np.zeros((4,5))
my_array[2, 0] = 3
my_array[1,3] = 5
print(my_array)

'''Create a snippet of Python code to create an ndarray of 5 rows and 5 columns filled with all numbers from 1 to 25.

Find the sum of the entire ndarray.

Find the following:

the mean of each row
the mean of each column
the maximum value in each row
the minimum value in each column'''
import numpy as np
my_array = np.arange(1,26).reshape(5,5)
print(my_array.sum())
print(np.mean(my_array, axis = 1))
print(np.mean(my_array, axis = 0))
print(np.max(my_array, axis = 1))
print(np.min(my_array, axis = 0))