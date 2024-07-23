import unittest
from typing import List
from minimax import find_best_move
from connectfour import C4Piece, C4Board
from board import Move


class TTTMinimaxCase(unittest.TestCase):
    def test_empty_position(self):
        all_empty_position: List[C4Piece] = [C4Board.Column(), 
                                             C4Board.Column(),
                                             C4Board.Column(),
                                             C4Board.Column(),
                                             C4Board.Column(),
                                             C4Board.Column(),
                                             C4Board.Column()]
        test_board1: C4Board = C4Board(all_empty_position, C4Piece.B)
        best_move: Move = find_best_move(test_board1, 5)
        self.assertEqual(best_move, 3)
        
    def test_easy_position(self):
        all_empty1_position: List[C4Piece] = [C4Board.Column([C4Piece.B]), 
                                             C4Board.Column([C4Piece.B]),
                                             C4Board.Column(),
                                             C4Board.Column([C4Piece.R]),
                                             C4Board.Column(),
                                             C4Board.Column(),
                                             C4Board.Column()]
        test_board2: C4Board = C4Board(all_empty1_position, C4Piece.R)
        best_move: Move = find_best_move(test_board2, 5)
        self.assertEqual(best_move, 1)
    
    def test_hard_position(self):
        all_empty2_position: List[C4Piece] = [C4Board.Column([C4Piece.B, C4Piece.B, C4Piece.R, C4Piece.R, C4Piece.R]), 
                                             C4Board.Column([C4Piece.B, C4Piece.R, C4Piece.R, C4Piece.R, C4Piece.R, C4Piece.B]),
                                             C4Board.Column([C4Piece.R, C4Piece.B, C4Piece.B]),
                                             C4Board.Column([C4Piece.B, C4Piece.R]),
                                             C4Board.Column([C4Piece.B, C4Piece.R, C4Piece.R, C4Piece.R, C4Piece.B, C4Piece.R]),
                                             C4Board.Column([C4Piece.B, C4Piece.B, C4Piece.R, C4Piece.R, C4Piece.R, C4Piece.B, C4Piece.B]),
                                             C4Board.Column([C4Piece.E, C4Piece.E])]
        test_board1: C4Board = C4Board(all_empty2_position, C4Piece.B)
        best_move: Move = find_best_move(test_board1, 5)
        self.assertEqual(best_move, 3)
    
    


            
if __name__ == "__main__":
    unittest.main()