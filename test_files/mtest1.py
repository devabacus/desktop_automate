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


import re

mstr = 'pg.moveTo(442,50, duration=0.8)'
# mstr = 'time.sleep(1.57)'
# mstr = "pg.mouseUp(button='left', x=442, y=50)"

def change_delay():
    ptrn = r'\d+.\d+'

def change_dur_value(mstr, value):
        ptrn = r'\d+\.\d+'
        old_dur = re.findall(ptrn, mstr)
        if old_dur:
            dur = old_dur[0]
            dur_num = round(float(dur) / value, 2)
            res = mstr.replace(dur, str(dur_num))
            return res
        return mstr
    
print(change_dur_value(mstr, 2))

# re.sub(r'.*duration=(\d+.\d+)', )


# pydirectinput.doubleClick(1000,300,duration=0.5,button='left')


