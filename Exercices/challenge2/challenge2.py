### Problem 2

### Write a Python program to display the current date and time.

### Helper: https://docs.python.org/3/library/datetime.html


import datetime
now = datetime.datetime.now ()
dateStr = now.strftime("%Y-%m-%d-%d %H:%M:%S")
print(f"Date and local Time into Djerba :{dateStr}")
