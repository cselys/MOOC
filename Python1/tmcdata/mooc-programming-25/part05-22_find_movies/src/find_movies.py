# Write your solution here
def find_movies(database: list, search_term: str):
    result = []
    for data in database:
        if search_term.lower() in data["name"].lower():
            result.append(data)
    return result
