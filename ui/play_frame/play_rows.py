from ui.texts import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.widgets import Widgets


    
def play_file_pick(parent_f, pathAct, on_pick_file):
    
    Widgets.lbl_ent_btn(parent_f=parent_f, lblName=FILE_PATH,
                        entVar = pathAct, btnName=BTN_DIR,
                        btnCallBack=on_pick_file, entWidth=40)
    
def opt_play(parent_f, speedVar, repeats, on_btn_play):
    
    btnPlay = ttk.Button(parent_f, text=BTN_PLAY, style=DANGER, command=on_btn_play)
    btnPlay.pack(padx=10, pady=10, side=RIGHT, anchor=SE)
    
    speed_f = ttk.Frame(parent_f)
    repeat_f = ttk.Frame(parent_f)
    Widgets.lbl_ent(parent_f=speed_f, lblName=LBL_SPEED, side=TOP,
                        entVar = speedVar)
    Widgets.lbl_ent(parent_f=repeat_f, lblName=LBL_REPEATS, side=TOP,
                        entVar = repeats)
    
    speed_f.pack(side=LEFT)
    repeat_f.pack(side=LEFT)


        