import threading
from core.record.main_rec import ActionRecorder
import ui.main_ui as ui
import threading
from core.play.main_play import *
import pathlib
from ui_core.constants.sett_consts import *
from ui_core.sett_handle import SETT
from ui.play_frame.play_frame import PlayFrame
from ui.rec_frame.rec_frame import RecFrame

class MainUiCore():
    
    def __init__ (self):
        _ui = ui.MainUi()
        self.recFrame = RecFrame(self)
        self.playFrame = PlayFrame(self)
        _ui.loop()
        
    def dir_path_handle(self,path):
        self.pathDir = path
        SETT.save_value(DIR_PATH, path)
    
    def on_opt_rec(self, opts):
        SETT.save_value(OPTS, opts)
        
    
    def start_record(self, fileName):
        self.filePath = self.recFrame.pathSave.get() + '/' + fileName + '.txt'
        print(fileName)
        SETT.save_value(FILE_NAME, fileName)
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
                     self.opts)

    def on_btn_play(self, filePath, opts):
        self.filePath = filePath
        self.opts =opts
        SETT.save_value(FILE_PATH, filePath)
        SETT.save_value(OPTS, opts)
        self.playThread = threading.Thread(target=self.run_play)
        self.playThread.start()
