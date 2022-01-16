import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui_core.sett_handle import SETT
from ui_core.constants.sett_consts import *


def init_vars(self):
        filePath = SETT.get_value(FILE_PATH)
        fileName = filePath.split('/')[-1].split('.')[0] if len(filePath) > 0 else ''
        self.pathSave = ttk.StringVar(value = SETT.get_value(DIR_PATH))
        self.pathAct = ttk.StringVar(value = filePath)
        self.fileName = ttk.StringVar(value = fileName)
        opts = SETT.get_value(OPTS)
        self.optSpeed = ttk.StringVar(value = opts[SPEED])
        self.optRepeats = ttk.StringVar(value = opts[REPEATS])
        self.status = ttk.StringVar(value = "Готов к записи")
        self.repeats = ttk.StringVar(value = "1")
        
def init_frames(self):
    self.dir_path_f = ttk.Frame()
    self.btn_file_f = ttk.Frame()
    self.start_act_f = ttk.Frame()
    self.rec_opts_f = ttk.Frame()
    self.dir_path_f.grid(row=0, column=0, padx=5, pady=(20,5), sticky=W)
    self.btn_file_f.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    self.start_act_f.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    self.rec_opts_f.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        