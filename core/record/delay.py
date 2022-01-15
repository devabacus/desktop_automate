import time

class Delay():
    
    def __init__ (self):
        self.last_time_act = round(time.perf_counter(),2)
    
    def get(self):
        delay = round(time.perf_counter(),2) - self.last_time_act
        self.last_time_act = round(time.perf_counter(), 2)
        delay = round(delay, 2) 
        # print(f'delay = {delay}, last_time_act = {self.last_time_act}')
        return delay
