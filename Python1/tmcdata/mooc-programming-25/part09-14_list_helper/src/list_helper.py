# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        count = {}
        res = my_list[0]
        for n in my_list:
            if n in count.keys():
                count[n] += 1
                if count[n] > count[res]:
                    res = n
            else:
                count[n] = 1
        return res 

    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for item in my_list:
            counts[item] = my_list.count(item)

        res = 0
        for value in counts.values():
            if value > 1:
                res += 1
        return res

