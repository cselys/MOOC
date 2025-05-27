# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    newboard = []
    print(game_board)
    if x < 0 or y < 0 or x > 2 or y > 2 or game_board[y][x] != '':
        return False
    print(game_board[0][0] )
    game_board[y][x] = piece
    print(game_board[0][0] )
    print(game_board)
    return True
