

import re


# def change_dur(mstr, value):
#         value = (100 - value_perc)/100
#         pattern = r'.*duration=(\d+.\d+)'
#         dur = re.findall(pattern, mstr)[0]
#         dur_num = round(float(dur) / value, 2)
#         res = mstr.replace(dur, str(dur_num))
#         return res
    
    
def change_delay(mstr, value):
        ptrn = r'\d+\.\d+'
        old_dur = re.findall(ptrn, mstr)
        if old_dur:
            dur = old_dur[0]
            dur_num = round(float(dur) / value, 2)
            res = mstr.replace(dur, str(dur_num))
            return res
        return mstr
