"""
List Methods:
    1.append()
    2.sort()
    3.reverse()
    4.count()
"""

myList = [45, 32, 65, 65, 1, 5, 2]
myList.append(56)
print(myList)

myList.sort()
print(myList)

myList.sort(reverse=True)
print(myList)

myList.reverse()
print(myList)

"""
Output:
original list --[45, 32, 65, 65, 1, 5, 2]
[45, 32, 65, 65, 1, 5, 2, 56] -- appended at last
[1, 2, 5, 32, 45, 56, 65, 65] -- sorted increasing by default
[65, 65, 56, 45, 32, 5, 2, 1] -- sorted decreasing as we passed reverse =true
[1, 2, 5, 32, 45, 56, 65, 65] -- just reverse the order whatever it was
"""

mylist = [1,2,3,1,2,5,2,5,2,3,2,1,5,2,25]
print(mylist.count(1))
print(mylist.count(2))
"""
count method counts the occurance of items 
in the list 
output:
3
6
"""

"""
copy(): returns the copy of list

list1 = list2 -- this is not correct way to copy
here list1 and list=2 both will be same only
reference will be changed
------------------
here copy() method comes for rescue
"""

mylists = [1,2,3,4,5]
mylist2 = mylists.copy()
mylist2[0] ='Changed in mylist2 only'
print(mylists)
print(mylist2)

"""
output:
[1, 2, 3, 4, 5]
['Changed in mylist2 only', 2, 3, 4, 5]
"""

"""
insert(): This method inserts an item at
the given index. User have to specify index and item 
to inserted
list.insert(index, item)
"""

list1= ["Hello","Welcome to Jungle"]
list1.insert(1,"Aditya")
print(list1)

"""
output:
['Hello', 'Aditya', 'Welcome to Jungle']
"""

"""
extend():
this methods adds an entire list or any other
collection datatypes like set, tuples, dict
to the existing list
"""

list1= ["Hello"]
list2= ["Aditya"]
list3= ["Welcome to Jugle"]
list4= []

list4.extend(list1)
print(list4)

list4.extend(list2)
print(list4)

list4.extend(list3)
print(list4)

"""
Output:
['Hello']
['Hello', 'Aditya']
['Hello', 'Aditya', 'Welcome to Jugle']
"""

"""
concatenating two lists:
list1+list2
"""
list1= ["Hello Aditya"]
list2= ["Welcome to Jungle"]
print(list1+list2)

"""
output:
['Hello Aditya', 'Welcome to Jungle']
"""