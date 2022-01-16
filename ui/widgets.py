from ui.texts import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Widgets():
    
    def lbl_ent_btn(parent_f, lblName, entVar, btnName, btnCallBack, entWidth, btnStyle = PRIMARY):
        Widgets.lbl_ent(parent_f, lblName, entVar, LEFT, entWidth)
        btnRec = ttk.Button(parent_f, text = btnName, style=btnStyle, command=btnCallBack)
        btnRec.pack(side = LEFT, padx=10, pady=10)

    def lbl_ent(parent_f, lblName, entVar, side = LEFT, entWidth=10):
        lbl = ttk.Label(parent_f, text=lblName, justify=CENTER)
        lbl.pack(side=side)
        fileEnt = ttk.Entry(parent_f, textvariable=entVar, width=entWidth)
        fileEnt.pack(side=side, padx=10, pady=10)
        
    