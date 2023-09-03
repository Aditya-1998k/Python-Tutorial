"""
Multiprocessing in Python:
"""
import multiprocessing
import requests

def downloadFile(url, name):
    print(f"started Downloading {name}")
    response = requests.get(url)
    open(f"multiprocessImage/multiprocessing{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")
    return "Downloaded"

# This url will give random image each time
url = "https://picsum.photos/2000/3000"
# This is the normal way
# for i in range(50):
#     downloadFile(url, i)
    
# Using Multiprocessing

"------------------------------------"
pros=[]
for i in range(50):
    p=multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pros.append(p)
    
for p in pros:
    p.join()

"""
THis will download fifty images using request, 
but all the request are concurrently it will
not wait for other to complete

--observation -- cpu usage reaches 100% during
the period
"""
