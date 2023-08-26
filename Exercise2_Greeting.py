import time;

hour =int(time.strftime('%H'))

if hour >0 and hour<12:
    print("Good Morning")
elif hour == 12:
    print("Good AfterNoon")
elif hour >12 and hour<17:
    print("Good Evening")
else:
    print("Good Night")