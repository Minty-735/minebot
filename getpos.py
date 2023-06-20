from Xlib import display

def get_cursor_position():
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]

while True:
    print("Координаты курсора (x, y):", get_cursor_position())
