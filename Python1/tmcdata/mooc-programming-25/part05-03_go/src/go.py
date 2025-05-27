# Write your solution here

def who_won(game_board: list):
    count1 = 0
    count2 = 0
    for row in game_board:
        count1 += row.count(1)
        count2 += row.count(2)
    if count1 == count2:
        return 0
    elif count1 > count2:
        return 1

    return 2