from game import *




def making_board(board_size: int) -> list[list[int]]:
    """Making the basic board for the game."""
    board = []
    for i in range(board_size):
        rows = []
        for j in range(board_size):
            rows.append(0)
        board.append(rows)
    return board


def taking_shot(board: list, shots: int, shot_x: int, shot_y: int):
    """Taking one shot and updating the board."""
    print(f"Please Choose the coordinates for the shot:
          \nYour remaining shots are {shots}:")
    shot_x = validating_or_terminating_key(input("Shot X -> "))
    shot_y = validating_or_terminating_key(input("Shot Y -> "))
    shot_x, shot_y = check_inbounds_shot(len(board), shot_x, shot_y)
    while True:
        if board[shot_y][shot_x] == 0:
            board[shot_y][shot_x] = "x"
            print("Bad Shot!!, You Missed...")
            shots -= 1
            return shots
        elif board[shot_y][shot_x] == 1:
            board[shot_y][shot_x] = "v"
            print("Good Shot!!!, You Hit A Submarine.")
            shots -= 1
            return shots
        else:
            print("You have already make a shot it this coordinates, please try again:"
                  "\n-- For terminating the game please press '*' --")
            shot_x = validating_or_terminating_key(input("Shot X -> "))
            shot_y = validating_or_terminating_key(input("Shot Y -> "))
            shot_x, shot_y = check_inbounds_shot(len(board), shot_x, shot_y)



def check_remaining_subs(board: list) -> bool:
    """Checks remaining subs on board"""
    count = 0
    for row in board:
        for i in row:
            if i == 1:
                count += 1
    return count


def check_inbounds_shot(size_board: int, shot_x: int, shot_y: int) -> bool:
    while not (shot_x < size_board and shot_y < size_board)
        print("You are out of the board please try again:")
        shot_x = validating_or_terminating_key(input("Shot X -> "))
        shot_y = validating_or_terminating_key(input("Shot Y -> "))
    return shot_x, shot_y
    


def check_not_to_match_subs(size_board: int, number_subs: int) -> bool:
    return (size_board ** 2) / 2 >= number_subs













# for i in making_board_bool(5):
#     print(*(str(j) for j in i))
