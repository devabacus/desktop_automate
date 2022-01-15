import threading
from core.record.main_rec import ActionRecorder
import ui.main_ui as ui
from ui.rec_frame import RecFrame
import threading

class MainUiCore():
    
    def __init__ (self):
        _ui = ui.MainUi()
        self.recFrame = RecFrame(self)
        _ui.loop()
        
    def dir_path_handle(self,path):
        self.pathDir = path
        print(path)
    
    def on_opt_rec(self, val):
        print(val)
    
    def start_record(self, fileName):
        self.filePath = self.recFrame.pathSave.get() + '/' + fileName + '.txt'
        self.recordThread = threading.Thread(target=self.run_record)
        self.recordThread.start()
        
    def run_record(self):
        ActionRecorder(self.filePath)

    def on_btn_play(self, filePath):
        print(f'start from {filePath}')
    

    # while True:
    #     time.sleep(10)
    
