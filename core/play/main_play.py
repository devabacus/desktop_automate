import pynput.mouse as ms
from pynput.mouse import Button

import pynput.keyboard as kb
from pynput.keyboard import Key
import time

mouse = ms.Controller()
keyboard = kb.Controller()


with open('actions.txt', encoding = 'utf8') as f:
    r = f.read()
    commands = r.split('\n')
    for comm in commands:
        exec(comm)        
quit()
