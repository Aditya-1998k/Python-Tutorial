"""
Drink Water Reminder
----------------------
Write a program which reminds you of
drinking water every hour or two. Your
Program can either beep or send desktop
notifications for a specific operating system.
"""
# xhost +local:
# run the aboe statment on the command line first if authorization issue
import time
import os
os.environ['DISPLAY'] = ':0'
import pyautogui as pag

def waterDrinkingNotificatioin(title, message):
    pag.alert(text=message, title=title)
    time.sleep(5)
    return

name = input("Enter your Name: ")
title = f"Attention {name}"
message = "Please Drink water Please Drink Water Please Drink Water"
while True:
    waterDrinkingNotificatioin(title, message)
    time.sleep(60*60)


"""
This program alert you every one hour
for drinking water
"""
