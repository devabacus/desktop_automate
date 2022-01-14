from cmd import Cmd
import time



class ActionRecorder():
    
    def __init__ (self, handler_func):
        self.actions = ''
        self.handler = handler_func
        self.dy = 0
        self.x = 0
        self.y = 0
        self.last_time_act = round(time.perf_counter(),2)
    
    def on_click(self, x, y, button, pressed):
        mouse_pos = ''
        delay = 0    
        delay = round(time.perf_counter(),2) - self.last_time_act
        self.last_time_act = round(time.perf_counter(), 2)
        self.actions += Cmd.SLEEP(delay)
        
        if self.dy != 0:
            self.actions += Cmd.MOUSE_SCROLL(self.dy)
            self.dy = 0
            
        if x != self.x and y != self.x:
            mouse_pos = Cmd.MOUSE_MOVE(x,y)
            self.x = x
            self.y = y
            
        self.actions += f'{mouse_pos}{Cmd.MOUSE_CLICK(pressed, button)}'
        if x == 0 and y == 0:
            self.handler(self.actions)
             
    def on_scroll(self, x, y, dx, dy):
        self.dy += dy