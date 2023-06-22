from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains # импортируем класс ActionChains из модуля action_chains

# import pyscreenshot as ps

driver = webdriver.Firefox()
options = Options()
# options.add_argument("--headless")

url = 'https://сапёр.com/'

driver.get(url)

index = 1
index = "tile" + str(index)
print("Ищем элемент с ID:", index)




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
            array[x][y] = element
    with open("test.txt","w")as f:    
        for x in range(weight):
            for y in range(hight):
                f.write(str(array[x][y]))
                f.write(" ")
            f.write('\n')
        


try:
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, index))
    )
except TimeoutException:
    print("Элемент с ID '{}' не найден за 10 секунд.".format(index))
    
element = driver.find_element(By.ID,"tile1")
  

click(element,driver)
 

get_matrix(9,9)


# driver.quit()
