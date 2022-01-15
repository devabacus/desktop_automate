import imghdr
from tkinter import PhotoImage
from tkinter import *
from ui.texts import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.paths import RecRows
from tkinter.filedialog import askdirectory, askopenfilename
from PIL import Image, ImageTk
from pathlib import Path

from ui.widgets import Widgets


class RecFrame():
    
    def __init__ (self, ui_core_obj):
        self.ui_core = ui_core_obj
        # RecRows()
        self.init_vars()
        self.init_frames()
        self.create_frames()
        
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
        
        
    def create_frames(self):
        RecRows.dir_path(self.dir_path_f, self.pathSave, self.on_dir_browse)
        RecRows.file_name_btn(self.btn_file_f, self.fileName, self.on_btn_rec, self.status)
        RecRows.act_file_pick(self.start_act, self.pathAct, self.on_pick_file, self.on_btn_play)
        RecRows.opt_rec(self.rec_opts, self.optVars, self.on_opt_rec)

    def on_btn_play(self):
        self.ui_core.on_btn_play(self.pathAct.get())
        
    def setStatus(self,status):
        self.status = status

    def on_pick_file(self):
        filePath = askopenfilename(title=ASK_FILE_TITLE)
        if filePath:
            self.pathAct.set(filePath)
            print(self.pathAct.get())
    
    def on_opt_rec(self):
        self.ui_core.on_opt_rec(self.optVars.get())
    
    def on_btn_rec(self):
        self.status.set("Идет запись...")
        self.ui_core.start_record(self.fileName.get())
        
    def on_dir_browse(self):
        dirPath = askdirectory(title=ASK_DIR_TITLE)
        if dirPath:
            self.pathSave.set(dirPath)
            self.ui_core.dir_path_handle(dirPath)
  

    
        