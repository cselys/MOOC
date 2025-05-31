# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    words = [ch for ch in string if ch not in forbidden]
    return "".join(words)