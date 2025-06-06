# Write your solution here
def search(products: list, criterion: callable):
    return [p for p in products if criterion(p)]