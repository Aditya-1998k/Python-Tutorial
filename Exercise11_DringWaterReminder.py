"""
Drink Water Reminder
----------------------
Write a program which reminds you of
drinking water every hour or two. Your
Program can either beep or send desktop
notifications for a specific operating system.
"""
import os
import time
# from plyer import notification

def waterDrinkingNotificatioin(title, message):
    os.system(f"espeak {title}")
    os.system(f"espeak {title}")
    os.system(f"espeak {message}")
    user = input("have you drink water: (Y/N): ")
    if user =='Y':
        return
    else:
        waterDrinkingNotificatioin(title, message)

name = input("Enter your Name: ")
interval = int(input("Enter the Interval in Minutes: "))
title = f"Attention {name}"
message = "Please Drink water Please Drink Water Please Drink Water"
while True:
    interval = interval*60*60
    waterDrinkingNotificatioin(title, message)
    time.sleep(interval)
    