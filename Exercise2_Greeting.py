import time;

timestamp =int(time.strftime('%H'))

if timestamp >4 and timestamp<12:
    print("Good Morning")
elif timestamp == 12:
    print("Good AfterNoon")
elif timestamp >12 and timestamp<21:
    print("Good Evening")
else:
    print("Good Night")