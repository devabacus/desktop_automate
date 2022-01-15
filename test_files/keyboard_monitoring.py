from pynput import keyboard

def on_press(key):
    print(type(key))
    print(key)
    print(str(key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
from pynput import keyboard

def on_press(key):
    print(key)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()