

def get_neighbors(x, y, width, height):
    neighbors = []
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

def get_F9(board):
    print("get_F9 begin")
    result = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            neighbor_values = get_neighbor_values(y, x, board)
            if "F" in neighbor_values and 9 in neighbor_values:
                c = x * len(board) + y
                result.append(c)
                # print(c)
    print("get_F9 end")
    return result

number_to_click =[]
def work(board):
    print("scan begin")
    result = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] in range(1,9):
                neighbor_values = get_neighbor_values(y, x, board)
                neighbor_9 = neighbor_values.count(9)
                neighbor_F = neighbor_values.count("F")
                if neighbor_9 == board[y][x] - neighbor_F:
                    b = [i for i in range(len(neighbor_values)) if neighbor_values[i] == 9]
                    for i in range(len(b)):
                        a = get_adjacent_coordinates(x,y,b[i],board)
                        if a != None:
                            c = a[0] * len(board) + a[1]
                            result.append(c)
                            print("__________   ")
                            print(c)
                elif neighbor_F == board[y][x]:
                    continue
                else:
                    board[y][x] -= neighbor_F
    print("scan end")
    click = get_F9(board)
    return result, click
    