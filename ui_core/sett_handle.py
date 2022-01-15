import shelve
import pathlib



class SETT():
    
    def get_value(sett_name):
        sett_file = str(pathlib.Path().absolute()) + '\settings'
        sett_value = ''
        with shelve.open(sett_file) as sett:
            if sett_name in sett:
                sett_value = sett[sett_name]
                sett.close()
                return sett_value                
            else: return ''
            
            
    def save_value(sett_name, sett_value):
        sett_file = str(pathlib.Path().absolute()) + '\settings'
        try:
            with shelve.open(sett_file) as sett:
                sett[sett_name] = sett_value
                sett.close()
        except:
            print("Файла настроек, или значения не существует")