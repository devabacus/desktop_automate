import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.texts import *
from ui_core.sett_handle import SETT
from ui_core.constants.sett_consts import *


def init_play_vars(self):
        self.pathAct = ttk.StringVar(value = SETT.get_value(FILE_PATH))
        opts = SETT.get_value(OPTS)
        self.optSpeed = ttk.StringVar(value = opts[SPEED])
        self.optRepeats = ttk.StringVar(value = '1')
        self.status = ttk.StringVar(value = STATUS_START)

        
def init_play_frames(self):
    self.start_act_f = ttk.Frame()
    self.rec_opts_f = ttk.Frame()
    self.start_act_f.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    self.rec_opts_f.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        