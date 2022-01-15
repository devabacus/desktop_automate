import pyautogui as pg

# pyautogui.drag(100, 100, 0.2, button='left')

# pg.moveTo(100,400,0.54)

def check_key(key):
    if key != k.ctrl_l:
        if '\\x01' in str(key): _key = "'a'"
        elif '\\x03' in str(key): _key = "'c'"
        elif '\\x16' in str(key): _key = "'v'"
        elif '\\x14' in str(key): _key = "'t'"
        else: _key = key 
        return _key
    return key
