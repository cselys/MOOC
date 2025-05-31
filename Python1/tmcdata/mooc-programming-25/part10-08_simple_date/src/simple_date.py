# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __eq__(self, another):
        if self.__day == another.__day and self.__month == another.__month and self.__year == another.__year:
            return True
        else:
            return False

    def __ne__(self, another):
        if self.__day != another.__day or self.__month != another.__month or self.__year != another.__year:
            return True
        else:
            return False

    def __lt__(self, another):
        if self.__year < another.__year:
            return True
        
        if self.__year == another.__year and self.__month < another.__month:
            return True

        if self.__year == another.__year and self.__month == another.__month and self.__day < another.__day:
            return True
        return False

    def __gt__(self, another):
        if self.__year > another.__year:
            return True
        
        if self.__year == another.__year and self.__month > another.__month:
            return True

        if self.__year == another.__year and self.__month == another.__month and self.__day > another.__day:
            return True
        
        return False