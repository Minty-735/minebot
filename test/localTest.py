from models import Board, Cell

board = Board(81)

# a = [0, 0, 1, 9, 0, 1, 2, 9, 1, 2, 9, 9, 9, 9, 9, 9]

a = [
0,0,1,9,9,9,9,9,9,
0,0,1,9,9,9,9,9,9,
0,1,2,9,9,9,9,9,9,
1,2,9,9,9,9,9,9,9,
9,9,9,9,9,9,9,9,9,
9,9,9,9,9,9,9,9,9,
9,9,9,9,9,9,9,9,9,
9,9,9,9,9,9,9,9,9,
9,9,9,9,9,9,9,9,9
]
for i, e in enumerate(a):
    cell = Cell(i, e)
    board.addcell(cell)
board.endBuild()

print(board, sep="\n")

board.calculate()
