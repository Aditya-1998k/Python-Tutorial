"""
Sets in python
sets are unordered collection of data
items. Sets are seperated by comma
within curly braces.
    1.Sets are unchangeable meaning we can
      not change once created
    2.Unordered cannot access by index
    3.Duplicate will be removed by sets
"""

s = {1, 2, 4, 5, 2, 1, 3, 2}
print(s)

info ={"Carla",19,False, 5.9, 19}
print(info)

test ={}
print(type(test))

for value in info:
    print(value)



"""
{1, 2, 3, 4, 5} --duplicate removed
{False, 19, 'Carla', 5.9} --order changed
<class 'dict'> --empty curly brace will be dict
------------------
we can use loop to access the items of sets
False
19
Carla
5.9
"""