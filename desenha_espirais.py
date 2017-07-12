import pyautogui
import time

x = 200
y = 200

time.sleep(5)
for i in range(30):
    pyautogui.dragRel(0, (-1*y), duration=0.25)
    x = x-4
    pyautogui.dragRel(x, 0, duration=0.25)
    y = y-4
    pyautogui.dragRel(0, y, duration=0.25)
    x = x-4
    pyautogui.dragRel((-1*x), 0)
    y = y-4
    
