"""
Async IO in Python
----------
Asynchronous I/O or async for short, is 
a programming pattern that allows for high
performance I/O operations in concurrent and 
non blocking manner.

asyncio -- module for ansynchronous funcions
"""
import asyncio
import requests

async def function1():
    URL = "https://images.unsplash.com/photo-1693155105117-944446f4df14?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80"
    response = requests.get(URL)
    open("image1.jpg", "wb").write(response.content)
    print("func1")
    return "Downloaded"

async def function2():
    URL = "https://images.unsplash.com/photo-1693154926673-200f6c02d991?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80"
    response = requests.get(URL)
    open("image2.jpg", "wb").write(response.content)
    print("func2")
    return "Downloaded"

async def function3():
    URL = "https://images.unsplash.com/photo-1668115250646-645fc8d88ba6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80"
    response = requests.get(URL)
    open("image3.jpg", "wb").write(response.content)
    print("func3")
    return "Downloaded"


# async def main():
#     await function1()
#     await function2()
#     await function3()
    
# asyncio.run(main())

"""
func1
func2
func3
---------
Here each function will run one by one
wait for previous to complete
--------------
To deal with this we can use asyncio.gather()
"""
async def main():
    List = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(List)

asyncio.run(main())
"""
func1
func2
func3
['Downloaded', 'Downloaded', 'Downloaded']
--------------
Here all are downloaded at the same time
They are executing parallely
"""
