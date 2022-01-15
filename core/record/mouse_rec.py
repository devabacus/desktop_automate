import time
from core.cmd import Cmd


class MouseRecorder():
    
    def __init__ (self, handle, delay):
        self.actions = ''
        self.handle = handle
        self.x = 0; self.y = 0
        self.delay = delay
        self.last_time_act = round(time.perf_counter(),2)
    
    def get_mouse_pos(self, x, y):
        if x != self.x and y != self.x:
            self.x, self.y = x,y
            return Cmd.MOUSE_MOVE(x,y)
        else: return ''
    
    def on_click(self, x, y, button, pressed):
        self.handle(Cmd.MOUSE_MOVE(x, y, self.delay.get()))
        self.handle(Cmd.MOUSE_CLICK(x,y,pressed,button))
             
    def on_scroll(self, x, y, dx, dy):
        self.handle(Cmd.MOUSE_MOVE(x,y, self.delay.get()) + Cmd.MOUSE_SCROLL(dy))
        
        
    def on_move(self, x, y):
        if abs(x-self.x) > 50 or abs(y-self.y) > 50:
            self.handle(Cmd.MOUSE_MOVE(x,y,self.delay.get()))
            self.x, self.y = x,y
            