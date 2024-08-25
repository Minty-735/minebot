from brain import work 
import numpy as np
board = [


[0,0,2,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[0,1,3,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[0,1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[1,2,2,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],

]


flag_list = set()
def flag100(mines):
    print("flag100 begin")
    # actions = ActionChains(driver) 
    for mine_id in mines:
        if mine_id not in flag_list:
            print(mine_id)
            # mine = driver.find_element(By.ID, mine_id)
            # actions.move_to_element(mine).context_click(mine).perform()
            # flag_list.add(mine_id)
    print("flag100 end")


mines = work(16,16,board)

flag100(mines)



