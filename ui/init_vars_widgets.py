import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def init_vars(self):
        self.pathSave = ttk.StringVar(value = "D:/Actions")
        self.fileName = ttk.StringVar(value = "actions")
        self.optVars = ttk.StringVar(value = "100%")
        self.pathAct = ttk.StringVar(value = "D:/Actions/actions.txt")
        self.status = ttk.StringVar(value = "Готов к записи")
        
def init_frames(self):
    self.dir_path_f = ttk.Frame()
    self.btn_file_f = ttk.Frame()
    self.start_act = ttk.Frame()
    self.rec_opts = ttk.Frame()
    self.dir_path_f.grid(row=0, column=0, padx=5, pady=(20,5), sticky=W)
    self.btn_file_f.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    self.start_act.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    self.rec_opts.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        