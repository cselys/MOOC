# Write your solution here:
class Series:
    def __init__(self, title:str, seasons:int, genres:list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        # self.rate = 0

    def rate(self,rating: int):
        self.ratings.append(rating)
        # self.rate = sum(self.ratings)/len(self.ratings)

    def __str__(self):
        rating_str = "no ratings"
        if self.ratings:
            count = len(self.ratings)
            rating_str = f"{count} ratings, average {sum(self.ratings)/count:.1f} points"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)} \n{rating_str}"

def minimum_grade(rating: float, series_list: list):
    res = []
    for item in series_list:
        rate = sum(item.ratings)/len(item.ratings)
        if rate >= rating:
            res.append(item)
    return res

def includes_genre(genre: str, series_list: list):
    res = []
    for item in series_list:
        if genre in item.genres:
            res.append(item)
    return res

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    seriest = [s1, s2, s3]
 
    answer = minimum_grade(4.5, seriest)
    print(answer)