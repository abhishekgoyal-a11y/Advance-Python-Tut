import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

919-890-1421
874.722.3211
874*722*3211
900-990-1711
800.272.7540

cat
mat
pat
bat

Ha Ha Ha

google.com

\d - Digit(0-9)
\D - Not a Digit(0-9)
\w - Word Character(a-z,A-Z,0-9, _)
\W - Not Word Character
\s - WhiteSpace(space,tab,newline)
\S - Not a WhiteSpace 

\b - Word Boundary
\B - Not a Word Boundary 
^  -  Begging of a String
$  - End of a string

Quantifiers:
* - 0 or More
+ - 1 or More
? - 0 or 1
{3} - Exact Number
{3,4} - range of number(Minimun and Maximum)


Mr. Abhishek
Mr Shivam
Mr Radhika
Mrs. Sakshi
Mr. T

abc.def@gmail.com
xyz@gmail.com
abc@gmail.com
pqr@gmail.com

xyz@gmail.com
abc@bennett.edu
pqr@outlook.net

stae@gmai.co4

https://www.google.com
http://corey.com
http://droppricealertherokuapp.com
https://youtube.com
https://gmail.com
https://www.nasa.gov

'''

sentence = "Hello my name is abhihsek goyal"

# Mobile Number Macthing

# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

#######################################################OR#######################################################

# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

# d1d2d3 either . or - d4d5d6 either . or - d7d8d910

# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# either 8 or 9 then 00 either . or - d4d5d6 either . or - d7d8d910

# pattern = re.compile(r'[^a-zA-Z]')

# It will print all character except a to z and A to Z 

# pattern = re.compile(r'[a-zA-Z]'))

# It will print all character from a to z and A to Z 

# pattern = re.compile(r'[^b]at')

# It exclude character 'b'

#######################################################OR#######################################################

# pattern = re.compile(r'[cmp]at')

# It also exclude character 'b'

# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w+')

# (Mr|Ms|Mrs)  :- Either of them 
# \.?\s        :- Either . or one space
# [A-Z]        :- One capital Character
# \w           :- Anyone from these "(a-z,A-Z,0-9, _)"
# *            :- Either one character from \w or all remaining character

# pattern = re.compile(r"[a-z]+@[a-z]+\.com")

# [a-z] first character is between a to z
# after first character we are checking next character until we got @ character
# after @ we are checking  character  from a to z until we get .
# last we are checking 'com'

# pattern = re.compile(r'[a-z]+\.?[a-z]+@[a-z]+\.(edu|net|com)')

# [a-z]+\.      :- first character is between a to z until we find .
# \.?[a-z]      :- either . or a to z
# [a-z]+@       :- a to z until we find @ 
# [a-z]+\.      :- a to z until we find .
# (edu|net|com) :- either of them

# pattern = re.compile(r'https?://(www\.)?\w+\.(com|gov)')

#######################################################OR#######################################################

pattern = re.compile(r'https?://(www\.)?([a-z]+)\.(com|gov)')

matches = pattern.finditer(text_to_search)

# re Methods
# finditer
# findall
# match 

# for match in matches:
	# print(match.group(1)) # print wwww if exists
	# print(match.group(2)) # print domain name
	# print(match.group(3)) # print com or gov if exists

for match in matches:
	print(match)


# Word Boundary :- space before every Word
# 				 "Ha HaHa" 
# 				 There are total 3 Ha present
# 				 first Ha then space Second Ha and then third Ha without any space 
# 				 So there are 2 word "Ha" which satisfy word Boundary