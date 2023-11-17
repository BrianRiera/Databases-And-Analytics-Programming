'''Task 3 (20 marks)
(a) Write a function that has one parameter that takes a string value as its argument.
The function should use regular expressions to check if the string contains decimal numbers. The
function should return the number of times decimal numbers appear in the string. Test your
function with multiple sample strings. [10 marks]
'''


'''\d+: This part of the pattern matches one or more digits. 
The \d is a shorthand character class that matches any digit (0-9), 
and the + quantifier means "one or more occurrences of the preceding pattern."

\.: This matches a literal dot (decimal point). In regular expressions, 
the dot . has a special meaning, so it needs to be escaped with a backslash \ to match a literal dot.

\d+: This part of the pattern again matches one or more digits.

|: This is the alternation operator, which acts like a logical OR.
It allows the pattern to match either the left side (decimal numbers with a decimal point) 
or the right side (whole numbers without a decimal point).

\d+: This part of the pattern matches one or more digits. It represents whole numbers without decimal points.

To summarize, the regular expression r'\d+\.\d+|\d+' matches two types of decimal numbers:

Decimal numbers with decimal points (e.g., 123.45):

\d+ matches one or more digits before the dot.
\. matches the dot.
\d+ matches one or more digits after the dot.
Whole numbers without decimal points (e.g., 123):

\d+ matches one or more digits representing whole numbers.'''
import re
def number_check(_text):
    # Regular expression pattern to match decimal numbers
    decimal_pattern = r'\d+\.\d+|\d+'
    # remove the |\d+ at end if only want decimals
    
    # Find all decimal numbers in the text
    decimal_numbers = re.findall(decimal_pattern, _text)
    
    # Count the number of decimal numbers found
    list_count = len(decimal_numbers)
    
    print(f'There are {list_count} decimal numbers in this text')

# Test the function with a sample text
sample_text = "The price of the item is $19.99 and the weight is 2.5 kg. and 7"
number_check(sample_text)  # Output: There are 2 decimal numbers in this text

'''(b) Write a function that has one parameter that takes a string value as its argument.
The function should use regular expressions to replace every occurrence of a tab character in the
string with four spaces. Test your function with multiple sample strings.'''

def replace_tab_with_space(string):
 return re.sub(r"\s+", " ", string)

#for tab you can use \t
old_text = """Hello my friends. How are you doing? I'm fine."""
old_text

new_text = replace_tab_with_space(old_text)
new_text


'''Given the following string:
Tweet Twoo Twitter Town
Have you seen a Toon too?
At noon in the townhall
The yellow sun soon shone.
a) Using a single regular expression, write a function to highlight the first and last 
characters in any given line. Your answer should look like this: 
{T}weet Twoo Twitter Tow{n}
{H}ave you seen a Toon too{?}
{A}t noon in the townhall{l}
{T}he yellow sun soon shone{.}
[15 marks]'''
import re
string = 'Tweet Twoo Twitter Town\nHave you seen a Toon too?\nAt noon in the townhall\nThe yellow sun soon shone.'
def highlight_first_and_last_characters(text):
    highlighted_text = re.sub(r'^(.)(.*)(.)$', r'(\1)\2(\3)', text, flags=re.MULTILINE)
    return highlighted_text
string = 'Tweet Twoo Twitter Town\nHave you seen a Toon too?\nAt noon in the townhall\nThe yellow sun soon shone.'
highlighted_text = highlight_first_and_last_characters(string)
print(highlighted_text)
'''Regular Expression: r'^(.)(.*)(.)$'

^: Matches the start of the line.
(.*): Captures any sequence of characters (except for a newline) and stores it in a group. 
The . matches any single character, and * means zero or more occurrences.
(.*): Another capturing group, similar to the one above.
$: Matches the end of the line.
So, the entire pattern captures the first character of the line, any characters in the middle, and the last character of the line.

Replacement Pattern: r'(\1)\2(\3)'

(\1): Refers to the first captured group, which is the first character of the line.
\2: Refers to the second captured group, which is any characters in the middle.
(\3): Refers to the third captured group, which is the last character of the line.
The replacement pattern encloses the first and last characters 
in curly braces and keeps the middle characters unchanged.

re.MULTILINE Flag:
The re.MULTILINE flag is used to indicate that the ^ and $ anchors should match
the start and end of each line in the input string (string). Without this flag,
^ and $ would match the start and end of the entire input string.

When you use re.sub(r'^(.)(.*)(.)$', r'(\1)\2(\3)', string, flags=re.MULTILINE),
it searches for lines in the string variable and applies the specified pattern.
For each line, it captures the first and last characters and replaces them with the pattern (\1)\2(\3),
effectively adding curly braces around the first and last characters
while keeping the middle characters unchanged. This results in the desired formatting as specified in the question.'''

'''b) Using another single regular expression, write another function that highlights 
the character string Tw . Your answer should look like this:
{Tw}eet {Tw}oo {Tw}itter Town
Have you seen a Toon too?
At noon in the townhall
The yellow sun soon shone'''

def highlight_tw_occurrences(text):
    highlighted_text = re.sub('Tw','{Tw}', text)
    return highlighted_text

# Given string
input_text = '''Tweet Twoo Twitter Town
Have you seen a Toon too?
At noon in the townhall
The yellow sun soon shone.'''

print(highlight_tw_occurrences(string))


import re

def highlight_repeated_characters(text):
    # Use a regular expression to find repeated characters and format them as required
    highlighted_text = re.sub(r'(\w)\1', r'\1{\1\1}', text)
    return highlighted_text

# Given string
input_text = '''Tweet Twoo Twitter Town
Have you seen a Toon too?
At noon in the townhall
The yellow sun soon shone.'''

# Call the function and print the result
highlighted_text = highlight_repeated_characters(input_text)
print(highlighted_text)

import re

def highlight_repeated_characters(text):
    # Use a regular expression to find repeated characters and format them as required
    highlighted_text = re.sub(r'(\w)(\1+)', r'{\1\2}', text)
    return highlighted_text

# Given string
input_text = '''Tweet Twoo Twitter Town
Have you seen a Toon too?
At noon in the townhall
The yellow sun soon shone.'''

# Call the function and print the result
highlighted_text = highlight_repeated_characters(input_text)
print(highlighted_text)

import re

def highlight_question_mark(text):
    # Use a regular expression to find a question mark and format it as required
    highlighted_text = re.sub(r'\?', r'{?}', text)
    return highlighted_text

print(highlight_question_mark(input_text))