import time
from core.cmds.mouse_cmds import MouseCmds


class MouseRecorder():
    
    def __init__ (self, handle, delay):
        self.actions = ''
        self.handle = handle
        self.x = 0; self.y = 0
        self.delay = delay
        self.cmd = MouseCmds()
        self.last_time_act = round(time.perf_counter(),2)
    
    def get_mouse_pos(self, x, y):
        if x != self.x and y != self.x:
            self.x, self.y = x,y
            return self.cmd.mouse_move(x,y)
        else: return ''
    
    def on_click(self, x, y, button, pressed):
        self.handle(self.cmd.mouse_move(x, y, self.delay.get()))
        self.handle(self.cmd.mouse_click(x,y,pressed,button))
             
    def on_scroll(self, x, y, dx, dy):
        self.handle(self.cmd.mouse_move(x,y, self.delay.get()) + self.cmd.mouse_scroll(dy))
        
    def on_move(self, x, y):
        if abs(x-self.x) > 3000 or abs(y-self.y) > 3000:
            self.handle(self.cmd.mouse_move(x,y,self.delay.get()))
            self.x, self.y = x,y
            