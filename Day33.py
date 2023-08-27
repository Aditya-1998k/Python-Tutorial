"""
Dictionary in Python:
    1.key value pair
    2.can directly access value using key
    3.dictionaries are ordered(python-3.7) collection of data
    4.seperated by commas and enclsed within curly
"""

dict = {
    "Aditya":"Human being",
    "Television":"NonLiving things",
    "spoon":"objects"
}

print(dict["Aditya"])
print(dict.get("Aditya")) 

print(dict.get("Aditya2"))
"""
-------------------------------------------
Human being
NonLiving things --this also same but not throw error if key does not exist
None --as this key does not exist
-------------------------------------------
print(dict["Aditya2"])
KeyError: 'Aditya2'  --as this key does not exist
"""

"""
Accessing all the values and keys
dict.keys()
dict.values()
"""

print(dict.keys())
print(dict.values())
# dict_keys(['Aditya', 'Television', 'spoon'])
# dict_values(['Human being', 'NonLiving things', 'objects'])

for key in dict.keys():
    print(f"the value corressponding to the {key} is {dict[key]}")

# the value corressponding to the Aditya is Human being
# the value corressponding to the Television is NonLiving things
# the value corressponding to the spoon is objects

for key, value in dict.items():
    print(f"the value for {key} is {value}")

# the value for Aditya is Human being
# the value for Television is NonLiving things
# the value for spoon is objects
