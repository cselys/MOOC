# Write your solution here:
class Clock:
    def __init__(self, hour: int, minutes: int, seconds: int):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        if self.hour == 23 and self.minutes == 59 and self.seconds == 59:
            self.hour = 0
            self.seconds = 0
            self.minutes = 0  
        elif self.minutes == 59 and self.seconds == 59:
            self.hour += 1
            self.seconds = 0
            self.minutes = 0          
        elif self.seconds == 59:
            self.seconds = 0
            self.minutes += 1
        else:
            self.seconds += 1
    
    def set(self, h:int, m: int):
        self.hour = h
        self.minutes = m
        self.seconds = 0

    def __str__(self):
        return f"{self.hour:02d}:{self.minutes:02d}:{self.seconds:02d}"