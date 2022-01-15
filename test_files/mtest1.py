import pyautogui as pg
import re
# pyautogui.drag(100, 100, 0.2, button='left')

# pg.moveTo(100,400,0.54)
key = '\'\\x14\''

if '\\x' in key:
    _key = str(key)
    _key = _key.replace('\\', '0')
    _key = re.findall(r'(0x.*)\'', _key)[0]
    num_chr = int(_key, 16) + 96
    mchar = chr(num_chr)
    print(mchar)

