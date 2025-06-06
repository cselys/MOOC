class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def sort_by_length(routes: list):
    def order_length(route: 'ClimbingRoute'):
        return route.length
    return sorted(routes, key=order_length, reverse=True)

def sort_by_difficulty(routes: list):
    def order_grade(route: 'ClimbingRoute'):
        return route.grade
    return sorted(sort_by_length(routes), key=order_grade, reverse=True)

# def sort_by_difficulty(routes: list):
#     def difficulty_order(route):
#         return (route.grade, route.length)