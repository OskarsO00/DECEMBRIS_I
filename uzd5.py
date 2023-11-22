import datetime

current_hour = datetime.datetime.now().hour

if current_hour < 12:
    print("Labrīt!")
elif current_hour < 18:
    print("Labdien!")
else:
    print("Labvakar!")