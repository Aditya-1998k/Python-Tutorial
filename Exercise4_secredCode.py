"""
write a python program to translate a message into
secret code language. Use the rules below
to translate normal english into secret code language
"""

"""
coding:
if the owrd contains atleas 3 character, remove the
first letter and append it at the end
now append three random characterat the starting and the end

eg: "aditya"
aditya ---dityaa
---kshdityaaksh

else:
simply reverse the string
eg:
adi--->ida
"""

"""
decoding:
if the word contain less than 3 character, reverse it
eg:ida--->adi

else:
remove the 3 random character from the start and end. Now 
remove the last letter and append it to the beginning
eg:
kshdityaaksh-->remove first 3 and last 3
dityaa-->remove last character and add at end
aditya
"""
import random
def encoding(str):
    alfa ="qwertyuiopasdfghjklzxcvbnm"
    if len(str)>3:
        str = str[1:]+str[:1]
        str1 = random.choice(alfa)
        str2 = random.choice(alfa)
        str3 = random.choice(alfa)
        str4=str1+str2+str3

        return str4+str+str4
    else:
        return str[::-1]
    
def decoding(str):
    if len(str)>3:
        str = str[3:len(str)-3]
        print(str)
        return str[len(str)-1]+str[0:len(str)-1]
    else:
        return str[::-1]
        

print(encoding("adi"))
print(decoding("ida"))