

from tkinter.filedialog import askopenfilename

from ui.texts import *
from ui_core.constants.sett_consts import *


def on_btn_play(self):
        self.ui_core.on_btn_play(self.pathAct.get(),
                                 {SPEED:self.optSpeed.get(), REPEATS:self.optRepeats.get()})
        
def setStatus(self,status):
    self.status = status

def on_pick_file(self):
    filePath = askopenfilename(title=ASK_FILE_TITLE)
    if filePath:
        self.pathAct.set(filePath)
        print(self.pathAct.get())
