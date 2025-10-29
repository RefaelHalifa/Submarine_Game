import random
from Course_EXE_Week_2.Submarine_Game.submarines.io import show_current_board, show_complete_board
from board import *



def place_subs(board: list[list[int]], number_of_subs: int):
    """Placing the subs on place"""
    for sub in range(number_of_subs):
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board) - 1)
        board[y][x] = 1


board_1 = making_board(5)
place_subs(board_1, 8)
for i in board_1:
    print(i)
print()

show_current_board(board_1)

taking_shot(board_1,3,2)

show_current_board(board_1)

taking_shot(board_1,3,2)

show_current_board(board_1)

show_complete_board(board_1)

