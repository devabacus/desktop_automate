from ui.texts import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Widgets():
    
    def lbl_ent_btn(parent_f, lblName, entVar, btnName, btnCallBack, entWidth, btnStyle = PRIMARY):
        lbl = ttk.Label(parent_f, text=lblName, justify=CENTER)
        lbl.pack(side=LEFT)
        fileEnt = ttk.Entry(parent_f, textvariable=entVar, width=entWidth)
        fileEnt.pack(side=LEFT, padx=10, pady=10)
        btnRec = ttk.Button(parent_f, text = btnName, style=btnStyle, command=btnCallBack)
        btnRec.pack(side = LEFT, padx=10, pady=10)

    def lbl_ent_vert(parent_f, lblName, entVar,entWidth=10):
        lbl = ttk.Label(parent_f, text=lblName, justify=CENTER)
        lbl.pack(side=TOP)
        fileEnt = ttk.Entry(parent_f, textvariable=entVar, width=entWidth)
        fileEnt.pack(side=TOP, padx=10, pady=10)