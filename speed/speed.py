from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from threading import Thread



firefox_options = Options()
firefox_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Firefox(options=firefox_options)




url = 'https://klik-test.ru/' #ссылка на сайт

driver.get(url)


wait = WebDriverWait(driver, 1)


element: WebElement = driver.find_element(By.XPATH, '//*[@id="clicker"]')
while 1:
    element.click()

# # c = board.get100mines()
# c = board.createGroup()
# c = list(set(c))
# print(*c,sep="\n")



