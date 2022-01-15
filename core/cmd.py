# class Cmd():
#     MOUSE_MOVE = lambda x,y: f'mouse.position = ({x},{y})\n'
#     MOUSE_CLICK = lambda isPress, btn: f'mouse.press({btn})\n' if isPress else f'mouse.release({btn})\n'
#     SLEEP = lambda x: f'time.sleep({round(x,2)})\n'
#     MOUSE_SCROLL = lambda x: f'mouse.scroll(0,{x})\n'
#     KEY_PRESS = lambda key: f'keyboard.press({key})\n'
#     KEY_RELEASE = lambda key: f'keyboard.release({key})\n'
    
    
    # keyboard.press(Key.space)
    # keyboard.release(Key.space)

# return comm
        
    # MOUSE_CLICK = lambda x,y,btn: f'pg.click({x},{y},button={str(btn).split(".")[1]})\n'
        

class Cmd():
    MOUSE_MOVE = lambda x,y, delay: f'pg.moveTo({x},{y}, duration={delay})\n'
    SLEEP = lambda delay: f'time.sleep({delay})\n'
    # MOUSE_SCROLL = lambda y: f'pg.scroll({y}00)\n'
    MOUSE_SCROLL = lambda y: f'mouse.scroll(0,{y})\n'
    
    def KEY_CMD(key, isPress):
        comm = 'pg.key'
        comm += 'Down' if isPress else 'Up'
        btn = ''
        if len(str(key)) == 3:
            comm += f'({key})\n'    
        else:
            btn = str(key).split(".")[1]
            if 'ctrl' in btn:
                btn = 'ctrl'
            comm += f'(\'{btn}\')\n'
        return comm
            
    
    def MOUSE_CLICK(x,y,pressed, btn):
        comm = 'pg.mouse'
        comm += 'Down' if pressed else 'Up' 
        comm += f'(button=\'{str(btn).split(".")[1]}\', '
        comm += f'x={x}, y={y})\n'
        return comm