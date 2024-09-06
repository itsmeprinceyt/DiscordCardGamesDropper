import pyautogui
import time
import keyboard
import random 

class AU:
    drop="sd"
    tag="st bd"

    def move_click(x,y):
        time.sleep(5)
        pyautogui.moveTo(x,y,duration=0.5)
        time.sleep(5)
        pyautogui.click()
    
    def press_enter():
        time.sleep(5)
        keyboard.press('enter')
    
    def paste_string(str):
        time.sleep(5)
        keyboard.write(str)


    def auto_drop_in_sofi():        
        #Auto Update
        AU.move_click(422,691)
        AU.paste_string(AU.drop)
        AU.press_enter()
        time.sleep(5)
        AU.move_click(410,470)
        AU.move_click(422,691)
        AU.paste_string(AU.tag)
        AU.press_enter()

time.sleep(10)
while(True):
    random_time = random.randint(450, 480)
    AU.auto_drop_in_sofi()
    time.sleep(random_time)