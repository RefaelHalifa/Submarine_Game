from submarines.io import validating_or_terminating_key


def get_shot_coordinates(board_size: int) -> tuple[int, int]:
    """Gets and validates shot coordinates from the user."""
    while True:
        shot_x = validating_or_terminating_key(input("Shot X -> "), is_coordinate=True)
        shot_y = validating_or_terminating_key(input("Shot Y -> "), is_coordinate=True)
        if check_inbounds_shot(board_size, shot_x, shot_y):
            return shot_x, shot_y
        else:
            print("You are out of the board please try again:")


def making_board(board_size: int) -> list[list[int]]:
    """Making the basic board for the game."""
    board = []
    for i in range(board_size):
        rows = []
        for j in range(board_size):
            rows.append(0)
        board.append(rows)
    return board


def taking_shot(board: list, shots: int) -> int:
    """Taking one shot and updating the board."""
    print(f"Please Choose the coordinates for the shot:\nYour remaining shots are {shots}:")
    board_size = len(board)

    while True:
        shot_x, shot_y = get_shot_coordinates(board_size)

        if board[shot_y][shot_x] == 0:
            board[shot_y][shot_x] = "x"
            print("Bad Shot!!, You Missed...")
            return shots - 1
        elif board[shot_y][shot_x] == 1:
            board[shot_y][shot_x] = "v"
            print("Good Shot!!!, You Hit A Submarine.")
            return shots - 1
        else:
            print("You have already make a shot it this coordinates, please try again:"
                  "\n-- For terminating the game please press '*' --")


def check_remaining_subs(board: list) -> bool:
    """Checks remaining subs on board"""
    count = 0
    for row in board:
        for i in row:
            if i == 1:
                count += 1
    return count


def check_inbounds_shot(size_board: int, shot_x: int, shot_y: int) -> bool:
    """Checks if shot is inside the board boundaries."""
    return 0 <= shot_x < size_board and 0 <= shot_y < size_board
