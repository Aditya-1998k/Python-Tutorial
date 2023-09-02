"""
Command Line Utility in Python
-------------
command line utilities are programs that 
run from the command line interface, they
are essential part of many development
workflows. In Python, you can create your
own command line utilities using the 
built-in argparse module.
eg: curl <--url--> --download <file-name>
try with index movie url
"""
import argparse
import requests

def download_file(url, local_fileName):
    if local_fileName is None:
        local_fileName = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_fileName, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_fileName

parser = argparse.ArgumentParser()
parser.add_argument("url", help = "Url of the file to download")
parser.add_argument("-o", "--output", help = "Name of the file", default=None)

args = parser.parse_args()

print(args.url)
print(args.output)
download_file(args.url, args.output)

"""
We created a command line utility to download file
using a method which requires url and file name if not
file name give it will extract from the url

parser = argparse.ArgumentParser()
created instance of argparse
added two arguments -- url and --output (optional)
to argument we can give data type also eg: type = int

args = parser.parse_args() --args made
we can run the file on terminal with two argument followed

eg: when with file name
python3 Day85.py https://www.cervantes.to/images/photo/2005/bailando.jpg --output bailando2.jpg

without filename
python3 Day85.py https://www.cervantes.to/images/photo/2005/bailando.jpg

"""