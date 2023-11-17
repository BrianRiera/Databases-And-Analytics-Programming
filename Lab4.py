'''1) Create a text file and manually add some data to the file
2) Write Python code to
 open the file for write only access
 attempt to read the contents of the file
3) Note the type of Error that has been raised.
4) Modify your code to
 use a try / except / finally construct that will catch the exception, print a userfriendly error message, and clean up the file resource
5) Investigate how you would create your own Exception class. Then create your own
Exception class and use it in your code from the previous exercise. 

'''
import io
try:
    # Open the file for write-only access
    with open(r'C:\Users\User\test_repo\classnotes.txt', 'w') as opened_file:
         # Assign the file object to the 'file' variable
        # Attempt to read the contents of the file
        content = opened_file.read()

except io.UnsupportedOperation:
    print("Error: Cannot read from a file opened in write-only mode.")
except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    try:
        # Close the file if it's open
        if file:
            file.close()
    except Exception as e:
        print(f"Error while closing the file: {e}")
# writing to a file overwrites file :()
with open(r'C:\Users\User\test_repo\classnotes.txt', 'w') as opened_file:
    opened_file.write('hellow this is a test')
    opened_file.write('\n This is a new line')

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

import practice_with_numpy as np

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

import practice_with_numpy as np
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

'''Regular Expresssions Exercise
1) Write a Python program that will identify URLs using regular expressions'''
import re
def find_urls(text):
    # Regular expression pattern to match URLs
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    # Find all URLs in the text using the regular expression pattern
    urls = re.findall(url_pattern, text)
    return urls

# Sample text containing URLs
sample_text = "Visit our website at https://www.example.com. For more info, go to http://example.org."

# Find and print URLs in the sample text
urls_found = find_urls(sample_text)
print("URLs found in the text:")
print(urls_found)


'''Text Analytics Exercise
1) Complete the tutorial at https://data-flair.training/blogs/nltk-python-tutorial/'''

import nltk
nltk.download()
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

text="Today is a great day. It is even better than yesterday. And yesterday was the best day ever."
from nltk.tokenize import sent_tokenize
sent_tokenize(text)

sent_tokenize("Hi, how are you? I'm good, you? Great!")
nltk.word_tokenize(text)
nltk.word_tokeni
nltk.word_tokenize("Last night, I went to Mrs. Martinez's housewarming. It was a disaster.")

from nltk.corpus import wordnet
syn=wordnet.synsets('love')
syn
syn[0].definition()
syn[0].examples()

syn=wordnet.synsets('life')
syn[0].definition()
syn[0].examples()
synonyms=[]
for syn in wordnet.synsets('AI'):
        for lemma in syn.lemmas():
               synonyms.append(lemma.name())
synonyms

antonyms=[]
for syn in wordnet.synsets('depressed'):
        for l in syn.lemmas():
                 if l.antonyms():
                          antonyms.append(l.antonyms()[0].name())
antonyms
from nltk.stem import PorterStemmer

# Create a Porter stemmer object
stemmer = PorterStemmer()

# Use the stemmer to stem a word
stemmed_word = stemmer.stem('loving')

# Print the stemmed word
print(stemmed_word)
stemmer.stem('trainee')
stemmer.stem('alibi')
stemmer.stem('formulae')
stemmer.stem('writing')

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize('believes')


#With ‘believes’, to work with a verb instead of a noun, use the ‘pos’ argument-

lemmatizer.lemmatize('believes',pos='v')


lemmatizer.lemmatize('crossing',pos='a') #adjective

lemmatizer.lemmatize('crossing',pos='v') #verb

lemmatizer.lemmatize('crossing',pos='r') #adverb

#Since lemmatizing gives us better results within context, it is often slower than stemming.
#We can filter NLTK stop words from text before processing it.
from nltk.corpus import stopwords
stopwords.words('english')


text="Today is a great day. It is even better than yesterday. And yesterday was the best day ever!"
stopwords=set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
words=word_tokenize(text)
wordsFiltered=[]
for w in words:
        if w not in stopwords:
                 wordsFiltered.append(w)
wordsFiltered

from nltk.tokenize import PunktSentenceTokenizer
text='I am a human being, capable of doing terrible things'
sentences=nltk.sent_tokenize(text)
for sent in sentences:
    print(nltk.pos_tag(nltk.word_tokenize(sent)))
