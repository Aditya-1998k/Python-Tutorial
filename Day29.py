"""
Docstring in python:
Python docstring are the string literal
that appears right after the function definition
which will describe about function
eg:input type, return etc
"""

def squere(num):
    """
    To get the squer of the number
    Keyword arguments:
    num -- integer
    Return: squere of number
    """
    return num*num

print(squere(5))
print(squere.__doc__)

"""
output:
25
function_name.__doc__
will return the docstring of python

To get the squer of the number
Keyword arguments:
num -- integer
Return: squere of number
"""

"""
pep8:
making python program readable
and less complex

open console
open repl
import this
and see the magic:
"""

"""
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""