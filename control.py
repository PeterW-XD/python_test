import pyautogui
import keyboard
import time

myStr = pyautogui.prompt(text='text', title='title', default='default')
myList = myStr.split()

pyautogui.moveTo(2200, 400, duration=1)
pyautogui.click()

for i in myList:
    pyautogui.typewrite(i + " meaning", interval=0.1)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.moveTo(100, 150, duration=1)
    pyautogui.click()
    time.sleep(3)
