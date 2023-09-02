"""
Using win32 api to pronounce the
name of person to shout
"""
import os
name = input("Enter the Your Name: ")

speechText = f"Good Job {name}"

os.system(f"espeak '{speechText}'")


"""
espeak --for linux and mac install -- sudo apt install espeak
"""