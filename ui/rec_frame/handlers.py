

from tkinter.filedialog import askdirectory

from ui.texts import ASK_DIR_TITLE


def on_btn_rec(self):
    self.status.set("Идет запись...")
    print(self.curRecOpt)
    self.ui_core.start_record(self.fileName.get())
        
def on_dir_browse(self):
    dirPath = askdirectory(title=ASK_DIR_TITLE)
    if dirPath:
        self.pathSave.set(dirPath)
        self.ui_core.dir_path_handle(dirPath)
  