"""
Methods of Sets:
sets in python work more or less
same as sets in mathematics
"""

"""
union() and update()
union--it will not change set1 and set2 and return
       union of both sets
update()--can update the existing sets
"""
s1={1,2,3,4,5}
s2={2,3,4,5,6,7}
print(s1.union(s2))
print(s1)
print(s2)

s1.update(s2)
print(s1)
print(s2)

"""
{1, 2, 3, 4, 5, 6, 7} --union of both
{1, 2, 3, 4, 5} --no change in set1
{2, 3, 4, 5, 6, 7}--no change in set2
{1, 2, 3, 4, 5, 6, 7} --set1 updated
{2, 3, 4, 5, 6, 7} --set2 unchanged
"""

"""
Intersection and intersection_update()
intersection -- no change in existin
intersection_update-- change existing
"""
cities ={"delhi","tokyo","bengaluru"}
cities2 ={"lucknow","patna","bengaluru"}

print(cities.intersection(cities2))

cities.intersection_update(cities2)
print(cities)

"""
{'bengaluru'} --no change in existing sets
{'bengaluru'} --changed cities set
"""

"""
symmetric_difference and symmetric_difference_update
----------------------------------------------------
symetic_diff = (A UNION B)- (A INTERSECTION B)
             = ALL THE UNCOMMON VALUE
"""
cities ={"delhi","tokyo","bengaluru"}
cities2 ={"lucknow","patna","bengaluru"}

print(cities.symmetric_difference(cities2))
print(cities)
print(cities2)
cities.symmetric_difference_update(cities2)
print(cities)

"""
{'lucknow', 'tokyo', 'delhi', 'patna'} --no existing change
{'tokyo', 'delhi', 'bengaluru'} --unchanged cities sets
{'patna', 'lucknow', 'bengaluru'} --unchanged cities2 sets
{'lucknow', 'tokyo', 'delhi', 'patna'} --changed cities set
"""

"""
isdisjoint()
this method checks if any items of the given
sets present in other sets
if presetn --return false
if not -- return true
"""

cities ={"delhi","tokyo","bengaluru"}
cities2 ={"lucknow","patna","bengaluru"}
print(cities.isdisjoint(cities2))

cities ={"delhi","tokyo","kolkata"}
cities2 ={"lucknow","patna","bengaluru"}
print(cities.isdisjoint(cities2))

"""
output:
False --bengaluru common
True --no common value
"""

"""
issuperset()--if set2 all item present in 
              set1 then set1 is superset of
              set2
issubset()--in the above case set2 is subset of
            set1
        
            set1 is superset of set2
            set2 is subset of set1
"""

cities ={"delhi","tokyo","bengaluru"}
cities2 ={"bengaluru"}

print(cities.issuperset(cities2))
print(cities2.issubset(cities))

"""
True -- all item of cities2 in cities1
True -- all item of cities2 in cities1
"""

"""
add()--add values in sets
update() -- update set1 with value of set2
remove() -- remove items from sets if 
            item not available raise error
discard() -- same as remove but not throw erro
           if not presents
pop() -- this method removes the last item of pop
         but we don't know which item as sets are
         unordered so we can store that in variable
         and check the value
del--del is not a method, it is a keyword which delete
       set itself
clear()--this methods clear all the items of the set
         and print the empty sets
in operator --to check if any value exist in sets or not
"""

set1={"potatoes","cauliflower"}
set2={"onion","ginger"}

set1.add("tomato")
print(set1)
set1.update(set2)
print(set1)
# output
# {'potatoes', 'tomato', 'cauliflower'}
# {'tomato', 'cauliflower', 'onion', 'potatoes', 'ginger'}


# set2.remove("gobhi")
# KeyError: 'gobhi'
set2.remove("onion")
print(set2)
# {'ginger'}

set2.discard("gobhi")
#even gobhi is present this will not throw error


print(set1)
item = set1.pop()
print(item)
# {'onion', 'potatoes', 'ginger', 'cauliflower', 'tomato'}
# onion  --sets are unordered so we cant predict last element

# del set2
# print(set2)
# NameError: name 'set2' is not defined. Did you mean: 'set1'?

if "cauliflower" in set1:
    print("today we will eat vegitable")
else:
    print("sorry order online")

# o/p-- today we will eat vegitable