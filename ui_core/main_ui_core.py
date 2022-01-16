import threading
from core.record.main_rec import ActionRecorder
import ui.main_ui as ui
from ui.rec_frame import RecFrame
import threading
from core.play.main_play import *
import pathlib
from ui_core.constants.sett_consts import *
from ui_core.sett_handle import SETT
from ui_core.sett_init import *

class MainUiCore():
    
    def __init__ (self):
        _ui = ui.MainUi()
        self.recFrame = RecFrame(self)
        initialize_setts(self.recFrame)
        _ui.loop()
        
    def dir_path_handle(self,path):
        self.pathDir = path
        SETT.save_value(DIR_PATH, path)
    
    def on_opt_rec(self, val):
        SETT.save_value(SPEED, val)
    
    def start_record(self, fileName):
        self.filePath = self.recFrame.pathSave.get() + '/' + fileName + '.txt'
        self.recordThread = threading.Thread(target=self.run_record)
        self.recordThread.start()
        
    def run_record(self):
        ActionRecorder(self.filePath, self.on_finish_rec)

    def on_finish_rec(self,count):
        self.recFrame.status.set(f'Записано {count}\n действий')
        
    def on_finish_play(self, comm):
        self.recFrame.status.set(comm)

    def run_play(self):
        play_actions(self.filePath,
                     self.on_finish_play,
                     self.recFrame.optVars)

    def on_btn_play(self, filePath):
        self.filePath = filePath
        SETT.save_value(FILE_PATH, filePath)
        self.playThread = threading.Thread(target=self.run_play)
        self.playThread.start()
