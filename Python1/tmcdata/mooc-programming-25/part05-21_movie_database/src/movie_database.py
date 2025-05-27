# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    my_record = {}
    my_record["name"] = name
    my_record["director"] = director
    my_record["year"] = year
    my_record["runtime"] = runtime
    database.append(my_record)
