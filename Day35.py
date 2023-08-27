"""
Python-else in Loop
-----------------------------
we can use else block after
loop iteration in python
we can use this with for loop and
while loop
---------------------------
if loop successfully completed --then
only it will execute
if break -- else block does not execute
"""

for i in range(4):
    print(i)
    if i ==3:
        break
else:
    print("sorry nothing else")

"""
output:
0
1
2
3
else block not executed as loop breaks
"""

for i in range(4):
    print(i)
else:
    print("sorry nothing else")

"""
0
1
2
3
sorry nothing else --executed as loop successfuly executed
"""
