from tkinter.filedialog import askdirectory
from ui.rec_frame.handlers import *
from ui.rec_frame.init_vars_rec import *
from ui.rec_frame.rows_rec_frame import *
from ui.texts import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.widgets import Widgets
from ui_core.constants.sett_consts import *
from ui_core.sett_handle import SETT

class RecFrame():
    
    def __init__ (self, ui_core_obj):
        self.ui_core = ui_core_obj
        init_rec_vars(self)
        init_rec_frames(self)
        self.create_frames()
    
    def create_frames(self):
        create_dir_path(self.dir_path_f, self.pathSave, lambda : on_dir_browse(self))
        create_file_name_btn(self, self.btn_file_f, self.fileName, lambda: on_btn_rec(self), self.status, self.recOpts)
        
    
    
    
        
        
        
        
   
   