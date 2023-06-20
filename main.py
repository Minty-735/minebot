# import pyscreenshot as ps
# from time import sleep
# sleep(2)
# image = ps.grab(bbox = (108, 376, 1074, 892))
# image.show()

img_to_numbers = {
"=":0,
"q":1,
"Q":2,
"I":3,
"G":4,
"i":5,
"L":6,
"w":7,
"E":8,
"3":10}


def img_to_nums(char: str) -> int:
    return img_to_numbers.get(char)


