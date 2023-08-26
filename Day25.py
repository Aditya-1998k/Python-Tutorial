"""
Manupulating Tuples:
-------------------
tuples are immutalbe so we cannot 
change anything in tuples
if you want then convert tuples to 
list and change and convert back
to tuples
"""
brics_countries =("Brazil","Russia",
                  "India","China","S Africa")

temp_list =  list(brics_countries)
temp_list.pop(3)
brics_countries = tuple(temp_list)
print(brics_countries)
# ('Brazil', 'Russia', 'India', 'S Africa')


"""
Output:
('Brazil', 'Russia', 'India', 'S Africa')
"""

"""
cancatanate two tuples
tuples3=tuple1+tuple2
"""
tup1 =("India",)
tup2 =("Bharat",)
tup3 =tup1+tup2

print(tup3)
# ('India', 'Bharat')

"""
count()--count of occurance of items
index()--return the index of first occurance
         tuple.index(element, start, end)
         it will check element bw start and end
"""

tuple1=(1,2,3,3,4,5,2,5,9,5,2,9,2,5)

print(tuple1.count(3))
print(tuple1.index(9))
print(tuple1.index(2,3,9))

"""
output:
2
8
6
"""




