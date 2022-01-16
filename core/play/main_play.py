import pynput.mouse as ms
from pynput.mouse import Button

import pynput.keyboard as kb
from pynput.keyboard import Key
import time
import pyautogui as pg
from test_files.mtest1 import change_dur_value
from ui.texts import FINISH_PLAY, WORK_PLAY_STATUS

from ui_core.constants.sett_consts import *
from core.utils import *

class MainPlay():
    
    def get_cmds(self, path):
        try: 
            with open(path, encoding = 'utf8') as f:
                r = f.read()
                return r.split('\n')
        except: print("No such a file")
    
    def play_actions(self, path, on_status, opts):
        
        mouse = ms.Controller()
        keyboard = kb.Controller()
        
        div = float(opts[SPEED])
        repeats = int(opts[REPEATS])
        
        cmds = self.get_cmds(path)
        rem_cmds = len(cmds)
        rem_rpts = repeats
        on_status(WORK_PLAY_STATUS(rem_rpts, rem_cmds))
        for item in range(0, repeats):
            for cmd in cmds:
                exec(change_delay(cmd,div))   
                rem_cmds -= 1     
                on_status(WORK_PLAY_STATUS(rem_rpts, rem_cmds))
            rem_rpts -= 1
        on_status(FINISH_PLAY(repeats))



