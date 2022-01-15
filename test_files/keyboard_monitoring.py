from pynput import keyboard

def on_press(key):
    print(str(key))
    # print(check_key(key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
from pynput import keyboard

def on_press(key):
    print(key)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
def check_key(key):
    if '\\x' in str(key): 
        
        _key = "'a'"
    elif '\\x03' in str(key): _key = "'c'"
    elif '\\x16' in str(key): _key = "'v'"
    elif '\\x14' in str(key): _key = "'t'"
    else: _key = key 
    return _key