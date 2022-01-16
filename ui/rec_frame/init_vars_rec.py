import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.texts import *
from ui_core.sett_handle import SETT
from ui_core.constants.sett_consts import *

def init_rec_vars(self):
    self.pathSave = ttk.StringVar(value = SETT.get_value(DIR_PATH))
    self.fileName = ttk.StringVar(value = SETT.get_value(FILE_NAME))
    self.recOpts = ['Все задержки', 'Только перемещений', 'Без задержек']
    self.curRecOpt = 'Иван'
    self.status = ttk.StringVar(value = '')
    
def init_rec_frames(self):
    self.dir_path_f = ttk.Frame()
    self.btn_file_f = ttk.Frame()
    self.dir_path_f.grid(row=0, column=0, padx=5, pady=(20,5), sticky=W)
    self.btn_file_f.grid(row=1, column=0, padx=5, pady=5, sticky=W)