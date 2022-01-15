from ui.texts import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

    
class PathPicker():
    
    def create(frame, pathVar, lblText, func_browse):
        path_row = ttk.Frame(frame)
        path_row.pack(fill=X, expand=YES, pady=5)
        path_lbl = ttk.Label(path_row, text = lblText)
        path_lbl.pack(side=LEFT, padx=(10,10))
        path_ent = ttk.Entry(path_row, textvariable=pathVar, width=50)
        path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        btn_path = ttk.Button(master = path_row, text="Выбрать", command=func_browse)
        btn_path.pack(side=LEFT, padx=5)
        
        
