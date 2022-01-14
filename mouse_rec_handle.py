from cmd import Cmd

class MouseRecorder():
    
    def __init__ (self, handle):
        self.actions = ''
        self.handle = handle
        self.x = 0; self.y = 0
    
    def get_mouse_pos(self, x, y):
        if x != self.x and y != self.x:
            self.x, self.y = x,y
            return Cmd.MOUSE_MOVE(x,y)
        else: return ''
    
    def on_click(self, x, y, button, pressed):
        self.handle(self.get_mouse_pos(x,y) + Cmd.MOUSE_CLICK(pressed, button))
             
    def on_scroll(self, x, y, dx, dy):
        self.handle(Cmd.MOUSE_MOVE(x,y) + Cmd.MOUSE_SCROLL(dy))
        
    # def on_move(self, x, y):
    #     self.x, self.y = x,y