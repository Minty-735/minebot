from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains # импортируем класс ActionChains из модуля action_chains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from pyvirtualdisplay import Display
url = 'https://сапёр.com/' #ссылка на сайт

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

display = Display(visible=0,size=(1024,768))
display.start()

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)


# driver = webdriver.Firefox()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


element = driver.find_element(By.ID,"tile1")

src = element.get_attribute("src")

actions = ActionChains(driver) 
actions.move_to_element(element) 
actions.click() 
actions.perform()

src_2 = element.get_attribute("src")

all_id = []




driver.quit()
display.stop()



# for i in range(15):
#     element = driver.find_elements
#     print()

'''
actions = ActionChains(driver) # создаем объект actions, который представляет набор действий с мышью и клавиатурой
actions.move_to_element(element) # добавляем действие перемещения курсора на элемент в набор actions
actions.click() # кликаем по элементу
actions.perform() # выполняем набор действий actions

grid = soup.find("div", {"id": "board"})
tiles = grid.find_all("img")

print(tiles)

driver.quit()
'''
