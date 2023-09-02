"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import requests

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

data ={
  "id": 0,
  "title": "string",
  "dueDate": "2023-09-02T15:08:55.717Z",
  "completed": True
}

headers = {
    'Content-type': 'application/json; charset = UTF-8'
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

"""
{"id":0,"title":"string","dueDate":"2023-09-02T15:08:55.717Z","completed":true}
What i have done:
I have take a fake api and tried post with some sample data
using requests module in python
"""
from bs4 import BeautifulSoup
url = "https://www.google.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)