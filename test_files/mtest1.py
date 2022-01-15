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


# pydirectinput.doubleClick(1000,300,duration=0.5,button='left')
pydirectinput.mouseDown(106,521)
time.sleep(0.1)
pydirectinput.mouseUp(106,521)
time.sleep(0.3)
pydirectinput.mouseDown(106,521)
time.sleep(0.1)
pydirectinput.mouseUp(106,521)
# pydirectinput.click(1067,703)
# pydirectinput.click(1000,280)
# time.sleep(0.3)
# pydirectinput.click(1000,280)
# time.sleep(0.3)
# pydirectinput.click(1000,280)

# keyboard.press(Key.cmd)
# time.sleep(0.3)
# keyboard.release(Key.cmd)

# pg.moveTo(100,400,0.54)
# time.sleep(2)
# pg.('win')
# time.sleep(2)
# pg.press('esc')
# time.sleep(2)
# pg.press('win')

