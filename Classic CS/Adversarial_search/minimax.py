from __future__ import annotations
from board import Piece, Board, Move


# find the best one from possible results for first player
def minimax(board: Board, maximizing: bool, original_player: Piece, max_depth: int = 8) -> float:
    # base case - have reached the final position
    # or max search depth     
    if board.is_win or board.is_draw or max_depth == 0:
        return board.evaluate(original_player)
    
    # Recursive case - maximize your benefit or minimize foe's benefit
    if maximizing:
        best_eval: float = float('-inf')
        # the random low starting point
        for move in board.legal_moves:
            result: float = minimax(board.move(move), False, original_player, max_depth - 1)
            best_eval = max(result, best_eval)
        return best_eval
    else:           # minimization
        worst_eval: float = float('inf')
        for move in board.legal_moves:
            result = minimax(board.move(move), True, original_player, max_depth - 1)
            worst_eval = min(result, worst_eval)
        return worst_eval
    
# Find the best possible turn from the current position, looking at max_depth turns ahead
def find_best_move(board: Board, max_depth: int = 8) -> Move:
    best_eval: float = float('-inf')
    best_move: Move = Move(-1)
    for move in board.legal_moves:
        result: float = minimax(board.move(move), False, board.turn, max_depth)
        if result > best_eval:
            best_eval = result
            best_move = move
    return best_move 