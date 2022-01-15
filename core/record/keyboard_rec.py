from core.cmd import Cmd
from pynput.keyboard import Key as k

# '\'\\x03\''

def check_key(key):
    if key != k.ctrl_l:
        if '\\x01' in str(key): _key = "'a'"
        elif '\\x03' in str(key): _key = "'c'"
        elif '\\x16' in str(key): _key = "'v'"
        elif '\\x14' in str(key): _key = "'t'"
        else: _key = key 
        return _key
    return key

class KeyboardRecorder():

    def __init__ (self, handle, delay):
        self.handle = handle
        self.delay = delay
      
    def on_press(self, key):
        self.handle(Cmd.SLEEP(self.delay.get()))
        self.handle(Cmd.KEY_CMD(check_key(key),True))

    def on_release(self,key):
        self.handle(Cmd.SLEEP(self.delay.get()))
        self.handle(Cmd.KEY_CMD(check_key(key),False))
        

