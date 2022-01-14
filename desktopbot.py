from pynput import mouse

class ActionRecorder():
    
    def __init__ (self, handler_func):
        self.actions = ''
        self.handler = handler_func
    
    def on_click(self, x, y, button, pressed):
         press_release = 'Pressed' if pressed else 'Released'
         self.actions += f'{button} {press_release} {(x, y)}\n'
         if x == 0 and y == 0:
             self.handler(self.actions)
             print("callback")
             

    def on_scroll(self, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    def on_release(x,y, dx, dy):
        print(f'release at {x},{y}')

    # Collect events until released


def write_to_file(actions):
    
    with open('actions.txt', 'w', encoding = 'utf8') as f:
        f.write(actions)


 
act = ActionRecorder(write_to_file) 
    
with mouse.Listener(
            # on_move=on_move,
            on_click=act.on_click,
            on_scroll=act.on_scroll) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
listener = mouse.Listener(
    # on_move=on_move,
    on_click=act.on_click,
    on_scroll=act.on_scroll,
    on_release = act.on_release
    )
listener.start()







