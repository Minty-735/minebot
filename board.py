board = [
[0,0,0,2,9,9,9,9,9,9,9,9,9,9,9,9,],
[1,1,1,2,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],

]


# print(len(board))
# print(len(board[0]))
def click_to_number():
    for i in range(len(board)):
        for j in range(len(board[i])):
            a = board[i][j]
            if not(a == 0 or a == 9):
                print(str(i*16+j),end=" ")
    print()    

a = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaBAMAAABbZFH9AAAAD1BMVEW9vb17e3v//wD///8AAABXk1meAAAAaElEQVQY043PwQnAIAyF4QgOUHGDRwYQuoCE7D9Tq41NoB76n/xO5lEJHVRPL0W1QrXRKm2VVV1ZAH0luOumjBGbBLO+pGAxZTxi0+yXeLxNJBBA/AdWhclv+d7pG3zfdnsqHh0lKkVdkaQgtF9LrKkAAAAASUVORK5CYII="

print(a[144])