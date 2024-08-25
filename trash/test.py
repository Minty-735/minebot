from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from models import Cell

firefox_options = Options()
firefox_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Firefox(options=firefox_options)

url = 'https://сапёр.com/' #ссылка на сайт


driver.get(url)


wait = WebDriverWait(driver, 1)
main_content = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="board"]')))

element: WebElement = driver.find_element(By.XPATH, '//*[@id="board"]')
tile_elements = element.find_elements(By.TAG_NAME, "img")

for tile in tile_elements:
    id = tile.get_attribute("id")
    src = tile.get_attribute("src")
    id = id.removeprefix("tile")
    cell = Cell(id, (src))
    board.addcell(cell)



driver.find_element(By.XPATH, '//*[@id="tile15"]').click()




