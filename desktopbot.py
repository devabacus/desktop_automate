from pynput import mouse
from mouse_rec_handle import ActionRecorder
import time
import sys

def write_to_file(actions):
    with open('actions.txt', 'w', encoding = 'utf8') as f:
        f.write(actions)
        f.close()
        

act = ActionRecorder(write_to_file) 

listener = mouse.Listener(
    on_click=act.on_click,
    on_scroll=act.on_scroll)
listener.start()



while True:
    time.sleep(10)


