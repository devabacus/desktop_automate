from core.cmd import Cmd
from pynput import mouse,keyboard
from core.record.keyboard_rec import KeyboardRecorder
from core.record.mouse_rec import MouseRecorder
import time

# keyboard._win32.KeyCode
class ActionRecorder():
    
    def __init__ (self):
        self.act_m = MouseRecorder(self.rec_handle)
        self.act_k = KeyboardRecorder(self.rec_handle)
        self.mouse_listen()
        self.keyboard_listen()
        self.actions = ''
        self.last_time_act = round(time.perf_counter(),2)
    
    def delay(self):
        delay = 0    
        delay = 0    
        delay = 0    
        delay = round(time.perf_counter(),2) - self.last_time_act
        self.last_time_act = round(time.perf_counter(), 2)
        return Cmd.SLEEP(delay)
    
    def write_to_file(self):
        with open('actions.txt', 'w', encoding = 'utf8') as f:
            f.write(self.actions)
            f.close()        

    def mouse_listen(self):
        listener = mouse.Listener(on_click=self.act_m.on_click,
                                  on_scroll=self.act_m.on_scroll)
                                #   on_move = self.act_m.on_move
        listener.start()           
    def keyboard_listen(self):
        listener = keyboard.Listener(on_press=self.act_k.on_press,on_release=self.act_k.on_release)
        listener.start() 

    def rec_handle(self, comm_str):
        self.actions += self.delay() + comm_str
        if 'keyboard.release(Key.esc)' in comm_str:
            self.write_to_file()
            exit()
            
