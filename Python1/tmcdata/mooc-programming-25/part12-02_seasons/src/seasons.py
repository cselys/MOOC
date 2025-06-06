# Write your solution here:
def sort_by_seasons(items: list):
    def sort_by_season(season:dict):
        return season["seasons"]
    return sorted(items, key=sort_by_season)