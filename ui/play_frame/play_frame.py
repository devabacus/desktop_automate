
from ui.play_frame.handlers import *
from ui.play_frame.init_vars_play import *
from ui.play_frame.play_rows import *


class PlayFrame():
    def __init__ (self, ui_core_obj):
        self.ui_core = ui_core_obj
        init_play_vars(self)
        init_play_frames(self)
        self.create_frames()
    
    
    def create_frames(self):
        
        play_file_pick(self.start_act_f, self.pathAct, lambda: on_pick_file(self))
        opt_play(self.rec_opts_f, self.optSpeed, self.optRepeats, lambda: on_btn_play(self))

