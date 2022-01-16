from core.cmds.mouse_cmds import MouseCmds
from pynput import mouse,keyboard
from core.record.delay import Delay
from core.record.keyboard_rec import KeyboardRecorder
from core.record.mouse_rec import MouseRecorder
import time

class ActionRecorder():
    
    def __init__ (self, filePath, on_stop_rec):
        self.filePath = filePath
        self.on_stop_rec = on_stop_rec
        self.delay = Delay()
        self.act_m = MouseRecorder(self.rec_handle, self.delay)
        self.act_k = KeyboardRecorder(self.rec_handle, self.delay)
        self.mouse_listen()
        self.keyboard_listen()
        self.actions = ''
        self.last_time_act = round(time.perf_counter(),2)
    
    def write_to_file(self):
        with open(self.filePath, 'w', encoding = 'utf8') as f:
            f.write(self.actions)
            f.close()        

    def mouse_listen(self):
        Listener = mouse.Listener(on_click=self.act_m.on_click,
                                  on_scroll=self.act_m.on_scroll,
                                  on_move=self.act_m.on_move)
        Listener.start()           
    def keyboard_listen(self):
        Listener = keyboard.Listener(on_press=self.act_k.on_press,on_release=self.act_k.on_release)
        Listener.start() 

    def rec_handle(self, comm_str):
        print(comm_str)
        self.actions += comm_str
        if 'esc' in comm_str:
            self.write_to_file()
            self.on_stop_rec(len(self.actions.split('\n')))
            exit()
                
