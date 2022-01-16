

from ui_core.sett_handle import SETT
from ui_core.constants.sett_consts import *


def initialize_setts(recFrame):
        filePath = SETT.get_value(FILE_PATH)
        fileName = filePath.split('/')[-1].split('.')[0] if len(filePath) > 0 else ''
        recFrame.pathSave.set(SETT.get_value(DIR_PATH))
        recFrame.optVars.set(SETT.get_value(SPEED))
        recFrame.pathAct.set(filePath)
        recFrame.fileName.set(fileName)