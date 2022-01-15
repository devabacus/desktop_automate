import threading
from core.record.main_rec import ActionRecorder
import ui.main_ui as ui
from ui.rec_frame import RecFrame
import threading

class MainUiCore():
    
    def __init__ (self):
        _ui = ui.MainUi()
        RecFrame(self)
        _ui.loop()
        
    def dir_path_handle(self,path):
        print(path)
    
    def on_opt_rec(self, val):
        print(val)
    
    def start_record(self, fileName):
        print(fileName)
        # self.recordThread = threading.Thread(target=self.run_record)
        
    def run_record(self):
        ActionRecorder()

    def on_btn_play(self):
        print("start play")
    

    # while True:
    #     time.sleep(10)
    
