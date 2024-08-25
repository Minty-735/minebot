from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains # импортируем класс ActionChains из модуля action_chains
import time
from brain import work
import numpy as np
# import pyscreenshot as ps

driver = webdriver.Firefox()
options = Options()
# options.add_argument("--headless")

url = 'https://сапёр.com/'

driver.get(url)
weight,hight = 16,16
index = 1
index = "tile" + str(index)


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
"3":9,
"p":"F"}

def img_to_nums(char) -> int:
    char = char[144]
    return img_to_numbers.get(char)

def get_neighbor_values(x, y, board):
    width, height = 16,16
    neighbors = get_neighbors(x, y, width, height)
    neighbor_values = [board[nx][ny] for nx, ny in neighbors]
    return neighbor_values

def click (element,driver):
    actions = ActionChains(driver) 
    actions.move_to_element(element) 
    actions.click() 
    actions.perform()

def get_matrix(weight, hight):
    print("get_matrix begin")
    array = [[0] * hight for i in range(weight)]

    for x in range(weight):
        for y in range(hight):
            index = x * hight + y
            index = "tile" + str(index)
            element = driver.find_element(By.ID, index)
            element = element.get_attribute("src")
            element = img_to_nums(element)
            array[y][x] = element

    with open("test.txt","w")as f:    
        for x in range(weight):
            f.write("[")
            for y in range(hight):
                f.write("")
                f.write(str(array[y][x]))
                f.write(",")
            f.write('],\n')
    print("get_matrix end")
    return array

flag_list = set()

def flag100(mines):
    print("flag100 begin")
    actions = ActionChains(driver) 
    for mine_id in mines:
        if mine_id not in flag_list:
            mine = driver.find_element(By.ID, "tile" + str(mine_id))
            actions.move_to_element(mine).context_click(mine).perform()
            flag_list.add(mine_id)
    sorted(flag_list)
    print(flag_list)
    print("flag100 end")

def click_to_number(board,numbers):
    actions = ActionChains(driver)
    print("click_to_number begin")
    print(numbers)
    for i in numbers:
        print(i)
        a = driver.find_element(By.ID,"tile"+str(i))
        actions.move_to_element(a) 
        actions.click() 
        actions.perform()
    print("click_to_number end")



    # actions = ActionChains(driver)
    # for i in range(len(board)):
    #     for j in range(len(board[i])):
    #         a = board[i][j]
            
    #         if not(a == 0 or a == 9 or a == "F "):
    #             actions.move_to_element(driver.find_element(By.ID,"tile"+str(j*16+i))) 
    #             print("tile"+str(j*16+i), a)
    #             actions.click() 
    #             actions.perform()
                
try:
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, index))
    )
except TimeoutException:
    print("Элемент с ID '{}' не найден за 10 секунд.".format(index))
    
element = driver.find_element(By.ID,"tile1")
  

dif = driver.find_element(By.ID,"difficulty") 
click(dif,driver)

time.sleep(1)
click(element,driver)


n = 0
time.sleep(1)
def test():
    board = get_matrix(weight,hight)
    mines,numbers = work(board)
    flag100(mines)
    click_to_number(board,numbers)
    print(mines)
    

while driver.find_element(By.ID,"face") != "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaBAMAAABbZFH9AAAAD1BMVEW9vb17e3v//wD///8AAABXk1meAAAAaUlEQVQY043PwQnAMAgFUAMZIJINxAECXSCI+89UE2wVmkM/Xh6R4AdMadCvSMkaCH3Ak3JUVQ1VIdJXQpbpqrTCLmEmm+kiWxVXtYc9rp1/YlVX/OniteeKW753Rofod+xeMAINs0rWDW08IHwPjv9jAAAAAElFTkSuQmCC":
    test()




# driver.quit()
