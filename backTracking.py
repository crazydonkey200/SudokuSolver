from sudoku import *

def backTrack(board):
    print board
    if iscomplete(board.CurrentGameboard): return board
    else:
        size = board.BoardSize
        for r in range(size):
            for c in range(size):
                if board.CurrentGameboard[r][c] != 0:
                    continue
                else:
                    for i in range(size):
                        if isLegalMove(board, r, c, i):
                            tryMove = backTrack(board.set_value(r, c, i))
                            if tryMove == False:
                                continue
                            else: return tryMove
                        else: continue
                                
    return False
                            
