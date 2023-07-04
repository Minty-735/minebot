

def get_neighbors(x, y, width, height):
    neighbors = []

    # Пройдись по каждой ячейке вокруг данной ячейки (x, y)
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x, new_y = x + i, y + j
            if (i == 0 and j == 0) or new_x < 0 or new_y < 0 or new_x >= width or new_y >= height:
                continue
            neighbors.append((new_x, new_y))
    return neighbors


def get_neighbor_values(x, y, board):
    width, height = 16,16
    neighbors = get_neighbors(x, y, width, height)
    neighbor_values = [board[nx][ny] for nx, ny in neighbors]
    return neighbor_values
    
def get_adjacent_element(x, y, choice, board):
    width, height = len(board[0]), len(board)

    # Определим смещение для каждой позиции
    offsets = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1)
    ]

    # Получаем координаты выбранного смещения
    offset_x, offset_y = offsets[choice]

    # Вычисляем координаты новой ячейки
    new_x, new_y = x + offset_x, y + offset_y

    # Проверь, не выходит ли новая ячейка за границы игрового поля
    if new_x < 0 or new_y < 0 or new_x >= width or new_y >= height:
        return None  # Возвращаем None, если выходит за границы

    return board[new_y][new_x]  # Возвращаем значение ячейки, если все в порядке
def get_adjacent_coordinates(x, y, choice, board):
    width, height = len(board[0]), len(board)

    # Определим смещение для каждой позиции
    offsets = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1)
    ]

    # Получаем координаты выбранного смещения
    offset_x, offset_y = offsets[choice]

    # Вычисляем координаты новой ячейки
    new_x, new_y = x + offset_x, y + offset_y

    # Проверь, не выходит ли новая ячейка за границы игрового поля
    if new_x < 0 or new_y < 0 or new_x >= width or new_y >= height:
        return None  # Возвращаем None, если выходит за границы

    return (new_x, new_y)  # Возвращаем координаты ячейки, если все в порядке



number_to_click =[]
def work(weight,hight,board):
    print("work begin")
    mines = []
    for y in range(weight):
        for x in range(hight):             
            neighbor_values = get_neighbor_values(y, x, board)
            if board[y][x] == 0 or board[y][x] == "F" or board[y][x] == 9:
                continue
            neighbor_9 = neighbor_values.count(9)
            if "F" in neighbor_values:
                neighbor_9 += neighbor_values.count("F")
            if  neighbor_9 == board[y][x] and board[y][x] != 0:
                c = x * weight + y
                if neighbor_values.count("F") == board[y][x]:
                    number_to_click.append(c)
                    print("__________   ")
                    print(c)
                b = [i for i in range(len(neighbor_values)) if neighbor_values[i] == "F" or neighbor_values[i] == 9]
                # print(board[y][x])
                for i in range(len(b)):
                    a = get_adjacent_coordinates(x,y,b[i],board)
                    if a != None:
                        mines.append(a)
    
    mines =  set(mines)
    mines_tile = []
    # print("-------------------------------------------")
    # print(sorted(number_to_click))
    for (x,y) in mines:
        
        a = (x * weight + y )
        mines_tile.append("tile"+str(a))
    # print(mines_tile)
    print("work end")
    return mines_tile, number_to_click


