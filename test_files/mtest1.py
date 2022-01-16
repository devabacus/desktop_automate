import time
import pyautogui
import pyautogui as pg
import re
import pynput.mouse as ms
from pynput.mouse import Button

import pynput.keyboard as kb
from pynput.keyboard import Key

import pydirectinput

# pyautogui.drag(100, 100, 0.2, button='left')
mouse = ms.Controller()
keyboard = kb.Controller()

pydirectinput.moveTo(265,264, duration=1.73)
pydirectinput.mouseDown(button='left', x=265, y=264)
pydirectinput.moveTo(265,263, duration=0.08)
pydirectinput.mouseUp(button='left', x=265, y=263)
time.sleep(1.68)
pydirectinput.keyDown('shift')
time.sleep(0.29)
pydirectinput.keyDown('end')
time.sleep(0.16)
pydirectinput.keyUp('end')
time.sleep(0.04)
pydirectinput.keyUp('shift')
time.sleep(2.84)
pydirectinput.keyDown('esc')



# pydirectinput.doubleClick(1000,300,duration=0.5,button='left')


