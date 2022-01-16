from tkinter import *
from tkinter.filedialog import askdirectory, askopenfilename
from ttkbootstrap.constants import *
from ui.init_vars_widgets import *
from ui.rec_rows import RecRows
from ui.texts import *

class RecFrame():
    
    def __init__ (self, ui_core_obj):
        self.ui_core = ui_core_obj
        init_vars(self)
        init_frames(self)
        self.create_frames()
        
           
    def create_frames(self):
        RecRows.dir_path(self.dir_path_f, self.pathSave, self.on_dir_browse)
        RecRows.file_name_btn(self.btn_file_f, self.fileName, self.on_btn_rec, self.status)
        RecRows.act_file_pick(self.start_act_f, self.pathAct, self.on_pick_file, self.on_btn_play)
        RecRows.opt_rec(self.rec_opts_f, self.optSpeed, self.optRepeats, self.on_opts_rec)

    def on_btn_play(self):
        self.ui_core.on_btn_play(self.pathAct.get())
        
    def setStatus(self,status):
        self.status = status

    def on_pick_file(self):
        filePath = askopenfilename(title=ASK_FILE_TITLE)
        if filePath:
            self.pathAct.set(filePath)
            print(self.pathAct.get())
    
    def on_opts_rec(self):
        self.ui_core.on_opt_rec({SPEED:self.optSpeed.get(), REPEATS:self.optRepeats.get()})
    
    def on_btn_rec(self):
        self.status.set("Идет запись...")
        self.ui_core.start_record(self.fileName.get())
        
    def on_dir_browse(self):
        dirPath = askdirectory(title=ASK_DIR_TITLE)
        if dirPath:
            self.pathSave.set(dirPath)
            self.ui_core.dir_path_handle(dirPath)
  

    
        