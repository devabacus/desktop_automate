class Cmd():
    MOUSE_MOVE = lambda x,y, delay: f'pg.moveTo({x},{y}, duration={delay})\n'
    SLEEP = lambda delay: f'time.sleep({delay})\n'
    MOUSE_SCROLL = lambda y: f'mouse.scroll(0,{y})\n'
    
    def KEY_CMD(key, isPress):
        comm = 'pg.key'
        comm += 'Down' if isPress else 'Up'
        btn = ''
        if '<' in str(key):
            btn = Cmd.num_key_convert(key)    
        elif '\\' in str(key):
            btn = Cmd.check_key(key)
        else: 
            if len(str(key)) == 3: 
                btn = str(key)[1:-1]
            else:
                btn = str(key).split(".")[1]
                if 'ctrl' in btn: btn = 'ctrl'
                if 'cmd' in btn: btn = 'win'
                
        comm += f'(\'{btn}\')\n'
        return comm
    
    
    def num_key_convert(key):
        num = int(str(key)[1:-1])
        btn = ''
        if num >95 and num < 106:
            btn = str(num - 96)
        elif num > 47 and num < 57:
            btn = str(num - 48)
        return btn
        
        
    
    def check_key(key):
        if key != k.ctrl_l:
            if '\\x01' in str(key): _key = "'a'"
            elif '\\x03' in str(key): _key = "'c'"
            elif '\\x16' in str(key): _key = "'v'"
            elif '\\x14' in str(key): _key = "'t'"
            else: _key = key 
            return _key
        return key
    
    
    
    def MOUSE_CLICK(x,y,pressed, btn):
        comm = 'pg.mouse'
        comm += 'Down' if pressed else 'Up' 
        comm += f'(button=\'{str(btn).split(".")[1]}\', '
        comm += f'x={x}, y={y})\n'
        return comm