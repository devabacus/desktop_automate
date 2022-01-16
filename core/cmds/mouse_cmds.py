import re


class MouseCmds():
    
    def mouse_move(x, y, delay):
        return f'pg.moveTo({x},{y}, duration={delay})\n'
    
    def sleep(delay):
        return f'time.sleep({delay})\n' 
    
    def mouse_scroll(y):
        return f'mouse.scroll(0,{y})\n'
    
    def mouse_click(x,y,pressed, btn):
        comm = 'pg.mouse'
        comm += 'Down' if pressed else 'Up' 
        comm += f'(button=\'{str(btn).split(".")[1]}\', '
        comm += f'x={x}, y={y})\n'
        return comm
    
    
class MouseShortCmds():
    
    def sleep(delay):
        return f'time.sleep({delay})\n' 
    
    def mouse_scroll(y):
        return f'mouse.scroll(0,{y})\n'
    
    def mouse_click(x,y, btn, double=False):
        if not double:
            comm = 'pg.click('
            if 'left' not in str(btn):
                comm += f'button=\'right\', '
        else: comm = 'pg.doubleClick('
        comm += f'x={x}, y={y})\n'
        return comm