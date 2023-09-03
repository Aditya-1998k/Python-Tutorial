"""
Regular Expression in Python:
regex--for short
it is powerful tool for working with string
and text data in python.
They allow you to match and manipulate strings
based on patterns, making it easy to perform
complex string operation with just a few lines
of code

import re --built in  module

Match Characters in regular expression
---------------
[]--Represent a character class
^ -- Matches the beginning
$ -- Matches the end
. -- Matches any character except newline
? -- Matches zero or one occurance
| -- Means OR (Matches with any of the character seperated by it)
* -- any number of occurance including 0 occurance
+ -- one or more occurance
"""

import re

text = """
Lorem Ipsum is simply dummy text of the 
printing and typesetting industry. 
Lorem Ipsum has been the industry's standard 
dummy text ever since the 1500s, when an 
unknown printer took a Gallery of type and 
scrambled it to make a type specimen book. 
It has survived not only five centuries, 
but also the leap into electronic typesetting, 
remaining Mallery unchanged. 
It was popularised in the 1960s with the 
release of Letraset sheets containing Lorem 
Ipsum passages, and more recently with desktop 
publishing Callery like Aldus PageMaker 
including versions of Lorem Ipsum.
"""
patterns = r"[A-Z]+allery"
match = re.search(patterns, text)
print(match)
"""
<re.Match object; span=(189, 196), match='Gallery'>

It will check patter where first character should by 
any A-Z alphabet
then 'allery'
+ -- one or more occurance
re.search -- stop at first search
"""
match = re.finditer(patterns, text)
for m in match:
    print(m.group())
    
"""
Gallery
Mallery
Callery

So we can use regex with different patterns
to make dealing with string easir

visit -- https://regexr.com/
"""
