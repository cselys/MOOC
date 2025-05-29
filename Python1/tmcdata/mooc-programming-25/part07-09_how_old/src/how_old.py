# Write your solution here
from datetime import datetime

day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))

born = datetime(year, month, day)
millennium = datetime(1999, 12, 31)
differ = millennium - born
if int(differ.days) < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {differ.days} days old on the eve of the new millennium.")