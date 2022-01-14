from cmd import Cmd
import time



class MouseRecorder():
    
    def __init__ (self, handle):
        self.actions = ''
        self.handle = handle
        self.dy = 0
        self.x = 0
        self.y = 0
        self.last_time_act = round(time.perf_counter(),2)
    
    def delay(self):
        delay = 0    
        delay = round(time.perf_counter(),2) - self.last_time_act
        self.last_time_act = round(time.perf_counter(), 2)
        self.handle(Cmd.SLEEP(delay))
    
    
    def on_click(self, x, y, button, pressed):
        mouse_pos = ''
        # self.delay()
        
        if self.dy != 0:
            self.handle(Cmd.MOUSE_SCROLL(self.dy))
            self.dy = 0
            
        if x != self.x and y != self.x:
            mouse_pos = Cmd.MOUSE_MOVE(x,y)
            self.x = x
            self.y = y
            
        self.handle(f'{mouse_pos}{Cmd.MOUSE_CLICK(pressed, button)}')
             
    def on_scroll(self, x, y, dx, dy):
        self.dy += dy