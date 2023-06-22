from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



def click (element,driver):
    actions = ActionChains(driver) 
    actions.move_to_element(element) 
    actions.click() 
    actions.perform()

def get_matrix(weight,hight):
    #array[weight][hight]
    array = [[0]* weight for i in range(hight)]
    for x in range(weight):
        for y in range(hight):
            index = x * weight + y
            index = "tile"+str(index)
            element = driver.find_element(By.ID,index)
            array[weight][hight] = element
    for x in range(weight):
        for y in range(hight):
            print(array[x][y],end = " ")
        print()
    

    
    # element.get_attribute("src")
    
get_matrix(9,9)



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


