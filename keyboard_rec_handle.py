from cmd import Cmd
import time


class KeyboardRecorder():

    def __init__ (self, handle):
        self.handle = handle
        self.last_time_act = round(time.perf_counter(),2)
    
    def delay(self):
        delay = 0    
        delay = round(time.perf_counter(),2) - self.last_time_act
        self.last_time_act = round(time.perf_counter(), 2)
        self.handle(Cmd.SLEEP(delay))

    def on_press(self, key):
        # self.delay()
        try:
            self.handle(Cmd.KEY_PRESS(key))
            
        except AttributeError:
            print(f'special key {key} pressed')

    def on_release(self,key):
        # self.delay()
        self.handle(Cmd.KEY_RELEASE(key))
        

