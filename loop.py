import pyautogui
import time
time.sleep(4)
c=0
while c<=20:
    pyautogui.typewrite("hello...")
    pyautogui.press("enter")
    c=c+1