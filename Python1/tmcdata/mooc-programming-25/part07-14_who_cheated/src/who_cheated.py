# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():    
    with open("start_times.csv") as my_file, open("submissions.csv") as my_sub:
        result = []
        start_dict = {}
        for line in csv.reader(my_file, delimiter=";"):
            start_dict[line[0]] = line[1]
        # print(start_dict)
        three_hour = timedelta(hours=3)
        for line in csv.reader(my_sub, delimiter=";"):
            start_time = datetime.strptime(start_dict[line[0]], "%H:%M")
            good_time = start_time + three_hour
            end_time = datetime.strptime(line[3], "%H:%M")
            if end_time > good_time:
                print(line[0], (end_time - start_time).total_seconds()//60//60)
                if line[0] not in result:
                    result.append(line[0])
        return result
