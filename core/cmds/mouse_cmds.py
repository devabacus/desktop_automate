import re


class MouseCmds():
    
    def mouse_move(self, x, y, delay):
        return f'pg.moveTo({x},{y}, duration={delay})\n'
    
    def sleep(self, delay):
        return f'time.sleep({delay})\n' 
    
    def mouse_scroll(self, y):
        return f'mouse.scroll(0,{y})\n'
    
    def mouse_click(self, x,y,pressed, btn):
        comm = 'pg.mouse'
        comm += 'Down' if pressed else 'Up' 
        comm += f'(button=\'{str(btn).split(".")[1]}\', '
        comm += f'x={x}, y={y})\n'
        return comm