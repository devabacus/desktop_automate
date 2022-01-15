import time
from core.cmd import Cmd
from core.record.delay import Delay

class MouseRecorder():
    
    def __init__ (self, handle, delay):
        self.actions = ''
        self.handle = handle
        self.x = 0; self.y = 0
        self.delay = delay
        self.last_time_act = round(time.perf_counter(),2)

    # def delay(self):
    #     self.delay = round(time.perf_counter(),2) - self.last_time_act
    #     self.last_time_act = round(time.perf_counter(), 2)
    #     return delay
    
    def get_mouse_pos(self, x, y):
        if x != self.x and y != self.x:
            self.x, self.y = x,y
            return Cmd.MOUSE_MOVE(x,y)
        else: return ''
    
    def on_click(self, x, y, button, pressed):
        # self.handle(self.get_mouse_pos(x,y) + Cmd.MOUSE_CLICK(pressed, button))
        self.handle(Cmd.MOUSE_MOVE(x, y, self.delay.get()))
        self.handle(Cmd.MOUSE_CLICK(x,y,pressed,button))
             
    def on_scroll(self, x, y, dx, dy):
        self.handle(Cmd.MOUSE_MOVE(x,y, self.delay.get()) + Cmd.MOUSE_SCROLL(dy))
        
    # def on_move(self, x, y):
    #     self.x, self.y = x,y