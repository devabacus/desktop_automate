class Cmd():
    MOUSE_MOVE = lambda x,y: f'mouse.position = ({x},{y})\n'
    MOUSE_CLICK = lambda isPress, btn: f'mouse.press({btn})\n' if isPress else f'mouse.release({btn})\n'
    SLEEP = lambda x: f'time.sleep({round(x,2)})\n'
    MOUSE_SCROLL = lambda x: f'mouse.scroll(0,{x})\n'
    KEY_PRESS = lambda key: f'keyboard.press({key})\n'
    KEY_RELEASE = lambda key: f'keyboard.release({key})\n'
    
    
    # keyboard.press(Key.space)
    # keyboard.release(Key.space)
