from cmd import Cmd
import time
from pynput.keyboard import Key as k

# '\'\\x03\''

def check_key(key):
    if key != k.ctrl_l:
        if '01' in str(key): 
           _key = "'a'"
        elif '03' in str(key): _key = "'c'"
        elif '16' in str(key): _key = "'v'"
        elif '14' in str(key): _key = "'t'"
        else: _key = key 
        return _key
    return key

class KeyboardRecorder():

    def __init__ (self, handle):
        self.handle = handle
      
    
      
    def on_press(self, key):
        try:
            self.handle(Cmd.KEY_PRESS(check_key(key)))
            # print(key)
            
        except AttributeError:
            print(f'special key {key} pressed')

    def on_release(self,key):
        self.handle(Cmd.KEY_RELEASE(check_key(key)))
        

