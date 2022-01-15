from core.cmd import Cmd
from pynput import mouse,keyboard
from core.record.delay import Delay
from core.record.keyboard_rec import KeyboardRecorder
from core.record.mouse_rec import MouseRecorder
import time

# keyboard._win32.KeyCode
class ActionRecorder():
    
    def __init__ (self):
        self.delay = Delay()
        self.act_m = MouseRecorder(self.rec_handle, self.delay)
        self.act_k = KeyboardRecorder(self.rec_handle, self.delay)
        self.mouse_listen()
        self.keyboard_listen()
        self.actions = ''
        self.last_time_act = round(time.perf_counter(),2)
    
    def write_to_file(self):
        with open('actions.txt', 'w', encoding = 'utf8') as f:
            f.write(self.actions)
            f.close()        

    def mouse_listen(self):
        listener = mouse.Listener(on_click=self.act_m.on_click,
                                  on_scroll=self.act_m.on_scroll)
        listener.start()           
    def keyboard_listen(self):
        listener = keyboard.Listener(on_press=self.act_k.on_press,on_release=self.act_k.on_release)
        listener.start() 

    def rec_handle(self, comm_str):
        print(comm_str)
        self.actions += comm_str
        if 'esc' in comm_str:
            self.write_to_file()
            exit()
            
