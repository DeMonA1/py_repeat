import unittest
from typing import List
from minimax import find_best_move
from tictactoe import TTTBoard, TTTPiece
from board import Move


class TTTDrawWinMovesCase(unittest.TestCase):
    def test_empty_position(self):
        all_empty_position: List[TTTPiece] = [TTTPiece.E, TTTPiece.E, TTTPiece.E, TTTPiece.E,
                                                TTTPiece.E, TTTPiece.E, TTTPiece.E, TTTPiece.E,
                                                TTTPiece.E]
        test_board1: TTTBoard = TTTBoard(all_empty_position, TTTPiece.X)
        answer_draw: Move = test_board1.is_draw
        answer_win: Move = test_board1.is_win
        self.assertEqual(answer_draw, False)
        self.assertEqual(answer_win, False)
        
    def test_win_position(self):
        to_win_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.X, TTTPiece.X, TTTPiece.O,
                                             TTTPiece.O, TTTPiece.X, TTTPiece.X, TTTPiece.O,
                                             TTTPiece.O]
        test_board2: TTTBoard = TTTBoard(to_win_position, TTTPiece.X)
        answer_draw: Move = test_board2.is_draw
        answer_win: Move = test_board2.is_win
        self.assertEqual(answer_draw, False)
        self.assertEqual(answer_win, True)
    
    def test_draw_position(self):
        to_draw_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.X, TTTPiece.O, TTTPiece.O,
                                             TTTPiece.O, TTTPiece.X, TTTPiece.X, TTTPiece.O,
                                             TTTPiece.O]
        test_board3: TTTBoard = TTTBoard(to_draw_position, TTTPiece.X)
        answer_draw: Move = test_board3.is_draw
        answer_win: Move = test_board3.is_win
        self.assertEqual(answer_draw, True)
        self.assertEqual(answer_win, False)
    
    def test_legal_moves_none(self):
        to_full_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.X, TTTPiece.O, TTTPiece.O,
                                             TTTPiece.O, TTTPiece.X, TTTPiece.X, TTTPiece.O,
                                             TTTPiece.O]
        test_board4: TTTBoard = TTTBoard(to_full_position, TTTPiece.X)
        answer_draw: Move = test_board4.legal_moves
        self.assertEqual(answer_draw, [])
    
    def test_legal_moves(self):
        to_position: List[TTTPiece] = [TTTPiece.E, TTTPiece.X, TTTPiece.O, TTTPiece.O,
                                             TTTPiece.O, TTTPiece.X, TTTPiece.X, TTTPiece.O,
                                             TTTPiece.E]
        test_board5: TTTBoard = TTTBoard(to_position, TTTPiece.X)
        answer_draw: Move = test_board5.legal_moves
        self.assertEqual(answer_draw, [0,8])

            
if __name__ == "__main__":
    unittest.main()