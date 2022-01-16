import pynput.mouse as ms
from pynput.mouse import Button

import pynput.keyboard as kb
from pynput.keyboard import Key
import time
import pyautogui as pg
from ui.texts import FINISH_PLAY, WORK_PLAY_STATUS

from ui_core.constants.sett_consts import *





def play_actions(fileActionsPath, on_status, opts):
    
    mouse = ms.Controller()
    keyboard = kb.Controller()
    
    speed = opts[SPEED]
    repeats = int(opts[REPEATS])
    
    with open(fileActionsPath, encoding = 'utf8') as f:
        r = f.read()
        cmds = r.split('\n')
        rem_cmds = len(cmds)
        rem_rpts = repeats
        on_status(WORK_PLAY_STATUS(rem_rpts, rem_cmds))
        for item in range(1, repeats):
            for cmd in cmds:
                exec(cmd)   
                rem_cmds -= 1     
                on_status(WORK_PLAY_STATUS(rem_rpts, rem_cmds))
            rem_rpts -= 1
        on_status(FINISH_PLAY(repeats))

