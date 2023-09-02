"""
Write a program to manipulate
pdf files using pyPDF. Your program
should be able to merge the multiple
pdf files into single pdf. 

pypdf --open source pure pdf library
capable of splitting, merging, cropping
and transforming the pages of pdf files.
It can also add custom data, viewing
options , and passwords to pdf files.
pypdf can retrieve text and metadata
from pdf as well.
"""
from PyPDF2 import PdfWriter
import os
merger = PdfWriter()
dir="/home/ubuntu/Downloads"

files = [file for file in os.listdir(dir) if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write({dir})
merger.close()
