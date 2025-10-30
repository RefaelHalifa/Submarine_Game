from submarines.board import making_board, taking_shot
from submarines.io import choosing_size_of_board, choosing_number_of_subs, choosing_number_of_shots, show_current_board
from submarines.placement import place_subs
from submarines.game import check_player_status


def main():
    # Game setup
    board_size = choosing_size_of_board()
    board = making_board(board_size)
    
    num_subs = choosing_number_of_subs(board_size)
    place_subs(board, num_subs)

    shots = choosing_number_of_shots()

    # Game loop
    while True:
        show_current_board(board)
        shots = taking_shot(board, shots)

        if check_player_status(board, shots):
            break

if __name__ == "__main__":
    main()