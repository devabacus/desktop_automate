import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainUi():
    
    def __init__ (self):
        self.root = ttk.Window()
        self.root.title("Actions")
        # self.create_rec_frame()
        
    def loop(self):
        self.root.mainloop()
    
    # def create_rec_frame(self):
        # self.rec_f = ttk.Frame()
        
    
    