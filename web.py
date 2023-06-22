from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from random import randint
from selenium.webdriver.common.action_chains import ActionChains # импортируем класс ActionChains из модуля action_chains

url = 'https://сапёр.com/' #ссылка на сайт



driver = webdriver.Firefox()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


element = driver.find_element_by_id("tile"+str(randint(40,60))) # находим элемент на странице по его id и присваиваем его переменной element
actions = ActionChains(driver) # создаем объект actions, который представляет набор действий с мышью и клавиатурой
actions.move_to_element(element) # добавляем действие перемещения курсора на элемент в набор actions
actions.click() # кликаем по элементу
actions.perform() # выполняем набор действий actions

grid = soup.find("div", {"id": "board"})
tiles = grid.find_all("img")

print(tiles)

driver.quit()



















# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--remote-debugging-port=9222')  # Добавим эту строку
# capabilities = webdriver.DesiredCapabilities.CHROME.copy()
# capabilities['acceptInsecureCerts'] = True
# for key, value in capabilities.items():
#     chrome_options.set_capability(key, value)
# driver = webdriver.Chrome(options=chrome_options)
