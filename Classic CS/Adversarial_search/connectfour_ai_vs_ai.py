from minimax import find_best_move
from connectfour import C4Board
from board import Move, Board

board: Board = C4Board()

def get_player_move() -> Move:
    player_move: Move = Move(-1)
    while player_move not in board.legal_moves:
        play: int = int(input('Enter a legal column (0-6):'))
        player_move = Move(play)
    return player_move

if __name__ == '__main__':
    # global game cycle
    while True:
        computer_move2: Move = find_best_move(board, 5)
        print(f'Computer move is {computer_move2}')
        board = board.move(computer_move2)
        print(board)
        if board.is_win:
            print('Computer 2 wins!')
            break
        elif board.is_draw:
            print('Draw!')
            break  
        computer_move: Move = find_best_move(board, 5)
        print(f'Computer move is {computer_move}')
        board = board.move(computer_move)
        print(board)
        if board.is_win:
            print('Computer 2 wins!')
            break
        elif board.is_draw:
            print('Draw!')
            break  