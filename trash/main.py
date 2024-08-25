
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


t5 = "BAAAAAQAgMAAABinRfyAAAACVBMVEW9vb3///97e3uVBMaVAAAAHklEQVQI12MIDQ0NARFBDAEMDFzkEl6rVq1i0AISAIlSC03msuDYAAAAAElFTkSuQmCC "
for i in range(len(t5)):
    if t5[i] == "3":
        print(i)



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
"3":9}
# 97

def img_to_nums(char) -> int:
    char = char[144]
    return img_to_numbers.get(char)

a = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb3///97e3uVBMaVAAAAHklEQVQI12MIDQ0NARFBDAEMDFzkEl6rVq1i0AISAIlSC03msuDYAAAAAElFTkSuQmCC "
print(img_to_nums(a))