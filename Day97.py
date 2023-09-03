"""
Multithreading in Python:
-----------
Multithreading is a technique in programming
that allows multiple threads of execution
to run concurrently within a single process.
In Python we can use threading module to implement
multithreading
"""
import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(4)
    print(f"Done for {seconds} second")
 
"""   
func(4)
func(2)
func(1)

This will execute one by one
suppose you went to restra and order three
things and there is one labour he will take
5 min for each dish
But what if we have 3 labour
All of them can start making concurrently
without waiting for others to complete
"""

"creating new thread"
t1 = threading.Thread(target=func, args=[4])
t2= threading.Thread(target=func, args=[3])
t3 = threading.Thread(target=func, args=[1])

start_time = time.time()
"starting the the thread and move on (it will run in background)"
t1.start()
t2.start()
t3.start()

"Waiting till t1, t2, t3 will not finish then it will move beyond"
t1.join()
t2.join()
t3.join()

print(time.time()- start_time)

""""
sleeping for 4 seconds
sleeping for 3 seconds
sleeping for 1 seconds
Done for 4 second
Done for 3 second
Done for 1 second

-----
wait for the function call t1, t2, t3 to be
complete then it will move on
4.0044050216674805
"""

"""
Thread Pool Executer --
We can use Thread Pool Executor for 
handling threading in python
"""
from concurrent.futures import ThreadPoolExecutor

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 4)
        future2 = executor.submit(func, 3)
        future3 = executor.submit(func, 2)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        
poolingDemo()

"""
sleeping for 4 seconds
sleeping for 3 seconds
sleeping for 2 seconds
Done for 4 second
None
Done for 3 second
None
Done for 2 second
None
-------------------------
Concurrently start all the function call
and then wait till all of them not get 
completed
"""

def poolingDemowithMap():
    with ThreadPoolExecutor() as executor:
        lists = [5,4,3,2]
        results = executor.map(func, lists)
        
        for result in results:
            print(result)

poolingDemowithMap()

"""
sleeping for 5 seconds
sleeping for 4 seconds
sleeping for 3 seconds
sleeping for 2 seconds
Done for 5 second
None
Done for 4 second
None
Done for 3 second
None
Done for 2 second
None
"""
