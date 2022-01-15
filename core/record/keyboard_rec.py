from core.cmd import Cmd
from pynput.keyboard import Key as k

# '\'\\x03\''



class KeyboardRecorder():

    def __init__ (self, handle, delay):
        self.handle = handle
        self.delay = delay
      
    def on_press(self, key):
        self.handle(Cmd.SLEEP(self.delay.get()))
        self.handle(Cmd.KEY_CMD((key),True))

    def on_release(self,key):
        self.handle(Cmd.SLEEP(self.delay.get()))
        self.handle(Cmd.KEY_CMD((key),False))
        

