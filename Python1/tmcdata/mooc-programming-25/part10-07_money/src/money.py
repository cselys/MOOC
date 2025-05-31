# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros + self.__cents / 100:.2f} eur"

    def __eq__(self, another):
        if self.__euros == another.__euros and self.__cents == another.__cents:
            return True
        return False

    def __ne__(self, another):
        if self.__euros != another.__euros or self.__cents != another.__cents:
            return True
        return False

    def __lt__(self, another):
        if self.__euros < another.__euros or (self.__euros == another.__euros and self.__cents < another.__cents):
            return True
        return False

    def __gt__(self, another):
        if self.__euros > another.__euros or (self.__euros == another.__euros and self.__cents > another.__cents):
            return True
        return False

    def __add__(self, another):
        c = self.__cents + another.__cents
        e = self.__euros
        if c >= 100:
            e += 1
            c -= 100
        e += another.__euros
        return Money(e,c)

    def __sub__(self, another):
        c = self.__cents
        e = self.__euros
        if c < another.__cents:
            e -= 1
            c += 100
        c -= another.__cents
        e -= another.__euros
        if e < 0:
            raise ValueError("negative")
        return Money(e,c)

if __name__ == "__main__":
    money1 = Money(1, 50)
    money2 = Money(1, 50)
    print(money1 + money2)