from minimax import find_best_move
from connectfour import C4Board
from board import Move, Board


class Game:
    def get_player_move(self) -> Move:
        player_move: Move = Move(-1)
        while player_move not in board.legal_moves:
            play: int = int(input('Enter a legal column (0-6):'))
            player_move = Move(play)
        return player_move
    
    def main(self):
        # global game cycle
        while True:
            human_move: Move = self.get_player_move()
            global board
            board = board.move(human_move)
            if board.is_win:
                print('Human wins!')
                break
            elif board.is_draw:
                print('Draw!')
                break
            computer_move: Move = find_best_move(board, 5)
            print(f'Computer move is {computer_move}')
            board = board.move(computer_move)
            print(board)
            if board.is_win:
                print('Computer wins!')
                break
            elif board.is_draw:
                print('Draw!')
                break
            
board: Board = C4Board()
game = Game()
game.main()