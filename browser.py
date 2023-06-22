from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# import pyscreenshot as ps
# from main import click

driver = webdriver.Firefox()
options = Options()
# options.add_argument("--headless")

url = 'https://сапёр.com/'

driver.get(url)

index = 1
index = "tile" + str(index)
print("Ищем элемент с ID:", index)

try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, index))
    )
except TimeoutException:
    print("Элемент с ID '{}' не найден за 10 секунд.".format(index))
    
# element = driver.find_element(By.ID,"tile1")
  

# click(element,driver)
'''
element = driver.find_element(By.ID, index) 



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
    


get_matrix(9,9)



driver.quit()
'''