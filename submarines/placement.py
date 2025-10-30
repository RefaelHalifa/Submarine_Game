import random
 
 
def place_subs(board: list[list[int]], number_of_subs: int):
    """Placing the subs on place"""
    subs_placed = 0
    board_size = len(board)
    while subs_placed < number_of_subs:
        x = random.randint(0, board_size - 1)
        y = random.randint(0, board_size - 1)
        if board[y][x] == 0:
            board[y][x] = 1
            subs_placed += 1
