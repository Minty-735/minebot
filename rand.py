from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains # импортируем класс ActionChains из модуля action_chains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from random import randint
from time import sleep

url = 'https://сапёр.com/' #ссылка на сайт


# driver = webdriver.Firefox()
driver = Firefox()
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
sleep(10)
all_id = []
elements = driver.find_elements(By.CSS_SELECTOR, "[id^='title']")
for i in elements:
    b = i.get_attribute("id")
    all_id.append(b)
driver.quit()

print(all_id)


with open("test_log.txt",'w') as file:
    file.writelines("\n".join(elements))
print(elements)





# for i in range(15):
#     element = driver.find_elements
#     print()
print("Полученный src элемента:", src[-3:])
print("После нажатия пуская клетка?",src_2[-3:])

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