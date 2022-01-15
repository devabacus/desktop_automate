from ui.texts import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.paths import PathPicker
from tkinter.filedialog import askdirectory


class RecFrame():
    
    def __init__ (self, ui_core_obj):
        self.rec_f = ttk.Frame()
        self.ui_core = ui_core_obj
        self.create_rec_path()
        
    def create_rec_path(self):
        self.pathSave = ttk.StringVar()
        PathPicker.create(self.rec_f, self.pathSave, SAVE_PATH, self.on_dir_browse)
        self.rec_f.grid(row=0, column=0)

    def on_dir_browse(self):
        dirPath = askdirectory(title=ASK_DIR_TITLE)
        if dirPath:
            self.pathSave.set(dirPath)
            self.ui_core.dir_path_handle(dirPath)