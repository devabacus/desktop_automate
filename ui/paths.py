from ui.texts import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.widgets import Widgets

class RecRows():
    
    def dir_path(frame, pathVar, func_browse):
        
        Widgets.lbl_ent_btn(parent_f=frame, lblName=SAVE_PATH,
                            entVar=pathVar, btnName=BTN_DIR,
                            btnCallBack=func_browse, entWidth=40)
        
    def file_name_btn(parent_f,fileNameVar, on_btn_rec):
        
        Widgets.lbl_ent_btn(parent_f = parent_f, lblName = LBL_FILE,
                            entVar = fileNameVar, btnName = BTN_REC,
                            btnCallBack = on_btn_rec, entWidth = 30)

    def act_file_pick(parent_f, pathAct, on_pick_file, on_btn_play):
        
        Widgets.lbl_ent_btn(parent_f=parent_f, lblName=FILE_PATH,
                            entVar = pathAct, btnName=BTN_DIR,
                            btnCallBack=on_pick_file, entWidth=40)
        
        btnPlay = ttk.Button(parent_f, text=BTN_PLAY, style=DANGER, command=on_btn_play)
        btnPlay.pack(padx=10, pady=10)


    def opt_rec(parent_f, speedVar, on_opt_rec):
        
        Widgets.lbl_ent_btn(parent_f=parent_f, lblName=LBL_SPEED,
                            entVar = speedVar, btnName=BTN_OPT,
                            btnCallBack=on_opt_rec, entWidth=15)
        
        
        
        
   
   