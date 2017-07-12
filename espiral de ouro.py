import pyautogui
import time

y = 0.5

time.sleep(5)
for i in range(20):
    pyautogui.dragRel(0, (-1*int(y)), duration=0.25)
    x = y * 1.618
    pyautogui.dragRel(int(x), 0, duration=0.25)
    y = x * 1.618
    pyautogui.dragRel(0, int(y), duration=0.25)
    x = y * 1.618
    pyautogui.dragRel((-1*int(x)), 0)
    y = x * 1.618
    
