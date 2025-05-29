# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observes = []

    def add_observation(self, observation: str):
        self.__observes.append(observation)

    def latest_observation(self):
        if len(self.__observes) == 0:
            return ""
        else:
            return self.__observes[-1]
    
    def number_of_observations(self):
        return len(self.__observes)

    def __str__(self):
        return f"{self.__name}, {len(self.__observes)} observations"
