import time
from core.cmds.mouse_cmds import MouseCmds, MouseShortCmds


class MouseRecorder():
    
    def __init__ (self, handle, delay, mode):
        self.mode = mode
        self.actions = ''
        self.handle = handle
        self.x = 0; self.y = 0
        self.delay = delay
        self.last_time_act = round(time.perf_counter(),2)
        self.last_cmd = ''
        
    
    def get_mouse_pos(self, x, y):
        if x != self.x and y != self.x:
            self.x, self.y = x,y
            return MouseCmds.mouse_move(x,y)
        else: return ''
    
    def on_click(self, x, y, button, pressed):
        if self.mode == 0:
            self.handle(MouseCmds.mouse_move(x, y, self.delay.get()))
            self.handle(MouseCmds.mouse_click(x,y,pressed,button))
        else:
            if pressed:
                 self.handle(MouseShortCmds.mouse_click(x,y,button))
            
    def on_scroll(self, x, y, dx, dy):
        self.handle(MouseCmds.mouse_move(x,y, self.delay.get()) + MouseCmds.mouse_scroll(dy))
        
    def on_move(self, x, y):
        if abs(x-self.x) > 3000 or abs(y-self.y) > 3000:
            self.handle(MouseCmds.mouse_move(x,y,self.delay.get()))
            self.x, self.y = x,y
            