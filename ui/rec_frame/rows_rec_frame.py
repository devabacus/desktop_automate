from tkinter.filedialog import askdirectory
from ui.play_frame.init_vars_play import *
from ui.rec_frame.handlers import *
from ui.texts import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.widgets import Widgets
from ui_core.constants.sett_consts import *
from ui_core.sett_handle import SETT



def create_dir_path(frame, pathVar, func_browse):
        
        Widgets.lbl_ent_btn(parent_f=frame, lblName=SAVE_PATH,
                            entVar=pathVar, btnName=BTN_DIR,
                            btnCallBack=func_browse, entWidth=40)
    
def recCombo(x):
    SETT.save_value(CUR_REC_TYPE, x.widget.current())
    x.widget.selection_clear()
    
def create_file_name_btn(obj, parent_f, fileNameVar, on_btn_rec, statusVar, recOpts):
        
        Widgets.lbl_ent(parent_f = parent_f, lblName = LBL_FILE,entVar = fileNameVar)
        recTypeCombo = ttk.Combobox(parent_f, values=recOpts, exportselection=0)
        cur_rec_type = SETT.get_value(CUR_REC_TYPE)
        recTypeCombo.current(cur_rec_type)
        recTypeCombo.selection_clear()
        recTypeCombo.pack(padx=10,pady=10, side=LEFT)
        recTypeCombo.bind("<<ComboboxSelected>>", lambda x: recCombo(x))    
        
        btnRec = ttk.Button(parent_f, text=BTN_REC, style=INFO, command=on_btn_rec)
        btnRec.pack(padx=10, pady=10, side=LEFT)
        
        lblStatus = ttk.Label(parent_f, textvariable=statusVar)
        lblStatus.pack(padx=10, pady=10)
