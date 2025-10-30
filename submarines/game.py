from submarines.board import check_remaining_subs
from submarines.io import wining_flow, losing_flow_0_shots, losing_flow_not_enough, show_complete_board


def check_player_status(status_board: list, shots: int):
    remaining_subs = check_remaining_subs(status_board)
    if remaining_subs > shots:
        if not shots:
            losing_flow_0_shots(status_board, shots, remaining_subs)
            return True
        else:
            losing_flow_not_enough(status_board, shots, remaining_subs)
            return True
    elif not remaining_subs:
        wining_flow(status_board, shots, remaining_subs)
        return True
    else:
        return False