# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date

def list_years(dates: list):
    res = []
    for d in dates:
        res.append(d.year)
    return sorted(res)