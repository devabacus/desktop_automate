import re

class KeyCmds():
    
    def __init__ (self):
        pass
    
    SLEEP = lambda self, delay: f'time.sleep({delay})\n' 
    
    def KEY_CMD(self, key, isPress):
        _key = str(key)
        comm = 'pg.key'
        comm += 'Down' if isPress else 'Up'
        btn = ''
        if '<' in _key:
            btn = self.num_key_convert(key)    
        elif '\\x' in _key:
            btn = self.check_key(_key)
        else: 
            if len(str(key)) == 3: 
                btn = str(key)[1:-1]
            else:
                btn = str(key).split(".")[1]
                if 'ctrl' in btn: btn = 'ctrl'
                if 'shift' in btn: btn = 'shift'
                if 'cmd' in btn: btn = 'win'
                if 'alt' in btn: btn = 'alt'
                
        comm += f'(\'{btn}\')\n'
        return comm
    
    
    def num_key_convert(self, key):
        num = int(str(key)[1:-1])
        btn = ''
        if num >95 and num < 106:
            btn = str(num - 96)
        elif num > 47 and num < 57:
            btn = str(num - 48)
        return btn
        
        
    
    def check_key(self, key):
        _key = key.replace('\\', '0')
        _key = re.findall(r'(0x.*)\'', _key)[0]
        num_chr = int(_key, 16) + 96
        mchar = chr(num_chr)
        return mchar
