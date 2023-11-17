
'''Write some Python code that creates an ndarray with 4 rows and 5 columns, filled with all zeros.
Set the value in the first column and 3rd row to be equal to 3. Set the value in the fourth column and second row to be equal 
to 5. Then print the contents of the ndarray'''

import numpy as np
my_array = np.zeros((4,5))
my_array[2, 0] = 3 # 3rd row 1st column
my_array[1,3] = 5 # 2nd row 4th column
print(my_array)

'''Create a snippet of Python code to create an ndarray of 5 rows and 5 columns filled with all numbers from 1 to 25.

Find the sum of the entire ndarray.

Find the following:

the mean of each row
the mean of each column
the maximum value in each row
the minimum value in each column'''

# Create a 5x5 NumPy array with values from 1 to 25 and reshape it into a 5x5 matrix
my_array = np.arange(1, 26).reshape(5, 5)

# Print the sum of all elements in the 5x5 array
print(my_array.sum())

# Print the mean (average) of each row in the 5x5 array (axis=1 calculates mean along rows)
print(np.mean(my_array, axis=1))

# Print the mean (average) of each column in the 5x5 array (axis=0 calculates mean along columns)
print(np.mean(my_array, axis=0))

# Print the maximum value of each row in the 5x5 array (axis=1 finds max value along rows)
print(np.max(my_array, axis=1))

# Print the minimum value of each column in the 5x5 array (axis=0 finds min value along columns)
print(np.min(my_array, axis=0))



# Create a NumPy array 'bork' containing integers from 0 to 59 (exclusive)
bork = np.arange(60) 
bork

# Reshape the 'bork' array into a 3-dimensional array with dimensions 3x4x5
bork = bork.reshape(3, 4, 5)
bork

# Extract a slice of the 'bork' array: from the third dimension (2nd index), take the third row (2nd index) and the first two elements (0:2)
b = bork[2, 2, 0:2]
b

# Define a function 'sumup' that calculates the sum of integers from 1 to 'n'
def sumup(n):
    total = 0
    # Iterate through integers from 1 to 'n' and accumulate the sum in 'total'
    for i in range(1, n + 1, 1):
        total = total + i
    return total

# Call the 'sumup' function with argument 5 and print the result (should return 15)
sumup(5)

# Import necessary libraries: scipy.stats for statistical functions and numpy as np for numerical operations
import scipy.stats as stats


# Sample data (replace this with your actual dataset)
data = np.array([142, 127, 171, 137, 161, 183, 148, 124])

# Calculate mean and standard deviation of the 'data' array
mean = np.mean(data)  # Calculate the mean (average) of the data
std_dev = np.std(data, ddof=1) #ddof=1 applies Bessel's correction (n-1) for sample standard deviation
sample_size = len(data)  # Determine the size of the sample (number of data points)




'''1) Create an array with the arange function and reshape the array as follows:
b = arange(24).reshape(2,3,4)
This gives us a 3-dimensional data structure – you can think of it as being like 2
spreadsheet sheets where each sheet contains 3 rows of data and each row contains
4 columns.
Using indexing and slicing perform the following tasks:
i) Choose the first set of 3 rows and 4 columns of data
ii) Choose the second row of data from the second set of 3 rows of data
iii) Choose all the data from the second column for both the first and second
sets of rows and columns of data
2) Use the ravel function to flatten the data. What’s the difference between ravel
and flatten?
3) Reshape the data so that there are 6 rows of 4 columns per row.
4) Get the transpose of the new data structure.
5) Restack the rows of the transposed data structure in reverse order (hint: look at the
row_stack function).
6) Split the resulting data structure horizontally (hint: look at the hsplit function).'''



b = np.arange(24).reshape(2,3,4)
b
c = b[0]
c
d = b[1,1,]
d
e = b[:,:,1]
e

arr = np.array([[1, 2, 3], [4, 5, 6]])
raveled_array = arr.ravel()

# Modifying raveled_array will affect the original array
raveled_array[0] = 100

print(arr)  # Output: [[100, 2, 3], [4, 5, 6]]

arr = np.array([[1, 2, 3], [4, 5, 6]])
flattened_array = arr.flatten()

# Modifying flattened_array will NOT affect the original array
flattened_array[0] = 100
print(arr)  # Output: [[1, 2, 3], [4, 5, 6]]


g = b.reshape(6,4)
g
h = g.transpose()
h
reversed_array = np.row_stack(h[::-1])
reversed_array

split_reverse = np.hsplit(reversed_array, 2)
split_reverse


'''NumPy Exercise 2
 The AAPL.csv contains some stock price data for Apple.
 The MSFT.csv contains some stock price data for Microsoft.
1) Use the loadtxt command to load data from AAPL.csv from columns 5 and 7 (i.e.,
the close price and the volume).
2) Based on the data provided, calculate the volume weighted average price for the
stock (i.e., calculate the average price using the volume as weight values).
3) Calculate the median value of the closing prices (hint: use the median function).
4) Calculate the variance value of the closing prices.
5) Again, use the loadtxt command to load data from columns 3 and 4 (i.e., the high
prices and the low prices).
6) Use the max and min functions to get the highest high and the lowest low value.
7) Load data from column 5 of AAPL.csv. Also, load data from column 5 of MSFT.csv.
8) Calculate the covariance matrix of the closing prices of AAPL and MSFT (hint: use the
cov function).
9) View the values on the diagonal (hint: diagonal).
10) Calculate the correlation coefficient of the closing prices of AAPL and MSFT (hint:
corrcoef). '''

AAPL = np.loadtxt('AAPL.csv', skiprows=1, delimiter=',', usecols=(4,6))
close_price = AAPL[:,0]
volume = AAPL[:,1]
vwap = np.sum(close_price*volume) / np.sum(volume)
print(f'Volume Weighted Average Price (vwap) for AAPL: {vwap:.2f}')
close_med = np.median(close_price)
print(f'Close Price Median was {close_med:.2f}')
close_var = np.var(close_price)
print(f'Close Price variance was {close_var :.2f}')

MSFT = np.loadtxt('MSFT.csv', skiprows=1, delimiter=',',usecols=(2,3))
high_price = MSFT[:,0]
low_price = MSFT[:,1]
max_high = np.max(high_price)
print(f'The highest high was {max_high:.2f}')
min_low = np.min(low_price)
print(f'The minimum low price was {min_low:.2f}')
MSFT_close = np.loadtxt('MSFT.csv', skiprows=1, delimiter=',',usecols=(4))

cov_close = np.cov(close_price, MSFT_close)
cov_close
diag_view = np.diag(cov_close)
diag_view
close_corrcoef = np.corrcoef(close_price, MSFT_close)
close_corrcoef


'''(a) Create a three dimensional NumPy ndarray containing all even numbers between 2000 and
3999. The resulting ndarray should be assigned to a variable and should have 4 layers, 50 rows and
5 columns. [5 marks]'''
import numpy as np
my_list = []
for i in np.arange(2000,3999):
    if i%2 ==0:
        my_list.append(i)
my_array = np.array(my_list).reshape(4,50,5)
my_array


'''(b) Compute the mean of the values for each of the first two rows in the second layer. The result should
be a 1D array with two separate values. [5 marks]'''

means = np.array([my_array[1][0].mean(), my_array[1][1].mean()])
means

'''(c) Compute the sum of all cells in the last three columns in all layers. The result should be a single
scalar value. [5 marks]'''

sum = np.sum(my_array[:,:,2:])
sum

'''(d) Using a single NumPy function, split the three dimensional array created in a) above row-wise,
producing four separate arrays. [5 marks]'''
split = np.split(my_array,4)

'''(e) Create two new ndarrays each containing 10 values. The first should have evenly spaced values from
20 to 60. The second should contain evenly spaced values from 10 to 30. Add together corresponding
array entry values from each of the two arrays, i.e. perform the addition element-wise. [5 marks]'''
import numpy as np

# Create the first ndarray with evenly spaced values from 20 to 60 (inclusive) with 10 elements
array1 = np.linspace(20, 60, 10)

# Create the second ndarray with evenly spaced values from 10 to 30 (inclusive) with 10 elements
array2 = np.linspace(10, 30, 10)

# Perform element-wise addition of the two arrays
result = array1 + array2

# Print the resulting array
print(result)


'''Question 2:
a) Create a 2-dimensional NumPy ndarray filled with 800 numbers. Ensure that your 
array has 100 rows and 8 columns.
[5 marks]'''

import numpy as np
my_numbers = np.arange(0,800).reshape(100,8)
my_numbers
'''Compute the sum of all entries in the first column.
Compute the sum of all entries in the last column.
[2 x 5 marks] '''
first_col_sum = np.sum(my_numbers[:,0])
first_col_sum
last_col_sum = np.sum(my_numbers[:,7])
last_col_sum

'''b) Using slicing, split this array into 5 separate arrays. The number of rows in each array 
should be equal, and there should still be 8 columns.
[10 marks]'''
'''Add together corresponding array entry values from each of the 5 arrays.
[5 marks] '''
my_numbers_split = np.vsplit(my_numbers,5)
my_numbers_split = np.split(my_numbers, 5, axis =0)
my_numbers_split


num_rows_per_array = my_numbers.shape[0] // 5
first_split = my_numbers[:20, :]
second_split = my_numbers[20:40,:]
third_split = my_numbers[40:60,:]
fourth_split = my_numbers[60:80,:]
fifth_split = my_numbers[80:100,:]

'''Add together corresponding array entry values from each of the 5 arrays.
[5 marks] '''
cumulative_array = np.add(first_split, second_split)
cumulative_array = np.add(cumulative_array, third_split)
cumulative_array = np.add(cumulative_array, fourth_split)
cumulative_array = np.add(cumulative_array, fifth_split)

cumulative_array


# Combine the arrays into a list
split_arrays = [first_split, second_split, third_split, fourth_split, fifth_split]

# Use np.add.reduce() to add arrays along the first axis (rows)
cumulative_array = np.add.reduce(split_arrays, axis=0)
cumulative_array


'''Question 2:
a) Create a 1-dimensional NumPy ndarray containing the first 200 even numbers.
[5 marks]'''

number_list = []
for number in range(400):
    if number%2 ==0:
        number_list.append(number)
my_array = np.array(number_list)
my_array
import numpy as np

# Create a NumPy ndarray containing the first 200 even numbers
even_numbers = np.arange(0, 400, 2)[:200]

# Print the resulting ndarray
print(even_numbers)



'''b) Modify the array so that the data is organised as a 2-dimensional array structure 
with 50 rows and 4 columns.
[5 marks]'''

new_array =my_array.reshape(50,4)

'''c) Using indexing and slicing perform the following tasks:
i. Choose all the data from the 4th column'''
fourth_column = new_array[:,3]

'''ii. Choose data from every second row'''

every_second_row_data = new_array[::2]

'''iii. Add together corresponding row entry values from the 2nd and 3rd
columns
[3 x 5 marks]'''
second_column = new_array[:,1]
third_column = new_array[:,2]
second_and_third = np.add(second_column,third_column)

