import pyautogui
import time

time.sleep(3)

f = open("FuckYouText", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
