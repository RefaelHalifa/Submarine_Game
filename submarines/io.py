import sys


def validating_or_terminating_key(key: str, is_coordinate: bool = False):
    """In every input of the game if the player presses '*' the game stops."""
    if key == "*":
        print("Exiting the game.....")
        sys.exit()
    while not key.isnumeric():
        key = input("You entered a non numeric value please try again: ")
        if key == "*":
            print("Exiting the game.....")
            sys.exit()

    value = int(key)
    if is_coordinate:
        return value - 1
    return value


def choosing_number_of_shots() -> int:
    choise = input("\nPlease choose an number of shots for the game:"
                   "\n -> ")
    return validating_or_terminating_key(choise)
 
def choosing_number_of_subs(board_size: int) -> int:
    choise = input("\nPlease choose an number of submarines for the game:"
                   "\n->  ")
    choise = validating_or_terminating_key(choise)
    while not check_not_to_match_subs(board_size, choise):
        choise = input("The number of submarines is too high for the size of the board, " \
                       "\nplease choose a lower number of submarines -> ")
        choise = validating_or_terminating_key(choise)
    return choise

def choosing_size_of_board() -> int:
    choise = input("\nPlease choose the size of the board for the game (e.g., 5 for a 5x5 board):"
                   "\nChoose one Number for 'Num * Num' board -> ")
    return validating_or_terminating_key(choise)


def check_not_to_match_subs(size_board: int, number_subs: int) -> bool:
    return (size_board ** 2) / 2 >= number_subs


def show_current_board(board: list):
    print()
    for row in board:
        for value in row:
            if value == 1:
                print(0, end=" | ")
            else:
                print(value, end=" | ")
        print()
    print()


def wining_flow(board: list, remaining_shots: int, remaining_subs: int):
    print(f"\nCongratulations you have WINED the game!!!!"
          f"\nThere are no more subs to kill!!"
          f"\nYour remaining shots are: {remaining_shots}"
          f"\nHere is the entire Board: ")
    show_complete_board(board)


def losing_flow_0_shots(board: list, remaining_shots: int, remaining_subs: int):
    print(f"\nWe are sorry, but you have LOST the game!!!!"
          f"\nThere are {remaining_subs} more subs to kill!!"
          f"\nAnd you have no more shot in the arsenal..."
          f"\nHere is the entire Board: ")
    show_complete_board(board)


def losing_flow_not_enough(board: list, remaining_shots: int, remaining_subs: int):
    print(f"\nWe are sorry, but you have LOST the game!!!!"
          f"You don't have enough Shots..."
          f"\nThere are {remaining_subs} more subs to kill!!!"
          f"\nAnd your remaining shots are: {remaining_shots}"
          f"\nHere is the entire Board: ")
    show_complete_board(board)


def show_complete_board(board: list):
    print()
    for row in board:
        for value in row:
            print(value, end=" | ")
        print()
    print()
