from cmd import Cmd


class KeyboardRecorder():

    def __init__ (self, handle):
        self.handle = handle

    def on_press(self, key):
        try:
            self.handle(Cmd.KEY_PRESS(key))
            
        except AttributeError:
            print(f'special key {key} pressed')

    def on_release(self,key):
        self.handle(Cmd.KEY_RELEASE(key))
        

