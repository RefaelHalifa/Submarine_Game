import sys
from board import check_remaining_subs
from io import wining_flow, losing_flow_0_shots, losing_flow_not_enough


def validating_or_terminating_key(key: str):
    """In every input of the game if the player presses '*' the game stops."""
    if key == "*":
        print("Exiting the game.....")
        sys.exit()
    while not key.isnumeric():
        key = input("You entered a non numeric value please try again: ")
    return int(key) - 1


# def check_remaining_shots(remaining_shots: int) -> bool:
#     if remaining_shots:
#         return True
#     return False

def check_player_status(status_board: list, shots: int):
    if check_remaining_subs(status_board) > shots:
        if not shots:
            losing_flow_0_shots(status_board, shots, check_remaining_subs(status_board))
            return True
        else:
            losing_flow_not_enough(status_board, shots, check_remaining_subs(status_board))
            return True
    elif not check_remaining_subs(status_board):
        wining_flow(status_board, shots, check_remaining_subs(status_board))
        return True
    else:
        return False