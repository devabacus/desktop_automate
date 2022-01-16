from core.cmds.keys_cmds import KeyCmds
from pynput.keyboard import Key as k

# '\'\\x03\''



class KeyboardRecorder():

    def __init__ (self, handle, delay):
        self.handle = handle
        self.delay = delay
        self.cmds = KeyCmds()
      
    def on_press(self, key):
        self.handle(self.cmds.SLEEP(self.delay.get()))
        self.handle(self.cmds.KEY_CMD((key),True))

    def on_release(self,key):
        self.handle(self.cmds.SLEEP(self.delay.get()))
        self.handle(self.cmds.KEY_CMD((key),False))
        

