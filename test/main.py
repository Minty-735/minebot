from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import models
from models import Cell, Board

from selenium import webdriver
from selenium.webdriver.firefox.options import Options










firefox_options = Options()
firefox_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Firefox(options=firefox_options)




url = 'https://сапёр.com/' #ссылка на сайт

driver.get(url)


board = Board(81)


img_to_numbers = {
    "=": 0,
    "q": 1,
    "Q": 2,
    "I": 3,
    "G": 4,
    "i": 5,
    "L": 6,
    "w": 7,
    "E": 8,
    "3": 9,
    "p": -1
}


def img_to_nums(char) -> int:
    char = char[144]
    return img_to_numbers.get(char)

def parse():
    element: WebElement = driver.find_element(By.XPATH, '//*[@id="board"]')
    tile_elements = element.find_elements(By.TAG_NAME, "img")

    for tile in tile_elements:
        id = tile.get_attribute("id")
        src = tile.get_attribute("src")
        id = int(id.removeprefix("tile"))
        cell: models.Cell = board.getCellById(id)
        cell.update(img_to_nums(src))
    board.updateinfo()


    # allTrue, allFalse = board.calculate()
    allTrue= board.get100mines()

    print("allTrue")
    print(allTrue)

    for i in allTrue:
        element = driver.find_element(By.XPATH, f'//*[@id="tile{i.id}"]')
        actions = ActionChains(driver)
        actions.context_click(element).perform()
        print(i)
        sleep(0.5)

    # print("allFalse")

    # for i in allFalse:
    #     element = driver.find_element(By.XPATH, f'//*[@id="tile{i}"]')
    #     element.click()
    #     print(i)
    # sleep(0.5)

    print("xd")
    for i in board.getActiveCells():
        element = driver.find_element(By.XPATH, f'//*[@id="tile{i.id}"]')
        element.click()
        print(i)
        sleep(0.5)




wait = WebDriverWait(driver, 1)


main_content = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="board"]')))

sleep(.5)

if 0:
    driver.find_element(By.XPATH, '//*[@id="difficulty"]').click()
    sleep(.5)
    driver.find_element(By.XPATH, '//*[@id="difficulty"]').click()
    sleep(.5)
    driver.find_element(By.XPATH, '//*[@id="difficulty"]').click()
    sleep(.5)


# main_content = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="board"]')))


element: WebElement = driver.find_element(By.XPATH, '//*[@id="board"]')
tile_elements = element.find_elements(By.TAG_NAME, "img")

for tile in tile_elements:
    id = tile.get_attribute("id")
    src = tile.get_attribute("src")
    id = id.removeprefix("tile")
    cell = Cell(id, img_to_nums(src))
    board.addcell(cell)


board.endBuild()

sleep(1)
driver.find_element(By.XPATH, '//*[@id="tile0"]').click()



while 1:
    sleep(1)
    print("start")
    parse()

    print(board)

# # c = board.get100mines()
# c = board.createGroup()
# c = list(set(c))
# print(*c,sep="\n")



