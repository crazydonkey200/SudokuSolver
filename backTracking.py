from sudoku import *

def backTrack(board, numSteps = 0, size = 0):
    numSteps += 1
    if size == 0: size = board.BoardSize
    if iscomplete(board.CurrentGameboard):
        print "\n this took us " + str(numSteps) + " steps"
        return board # this prints the board
    else:
        for r in range(size):
            for c in range(size):
                if board.CurrentGameboard[r][c] != 0: continue
                else:
                    for i in range(1, size+1):
                        if isLegalMove(board, r, c, i):
                            board.set_value(r, c, i)
                            tryMove = backTrack(board, numSteps, size)
                            if tryMove == False:
                                board.set_value(r, c, 0)
                                continue
                            else: return tryMove
                        else:
                            continue
                    return False ## if we can't put anything in an open spot, we can stop right now.
    return False
                            
