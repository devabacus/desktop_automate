

LBL_FILE = "Название\n экшена"
BTN_REC = "Начать запись"
LBL_SPEED = "Ускорение"
LBL_REPEATS = "Повторений"
BTN_SAVE_OPT = "Сохранить"
FILE_PATH = "Файл экшена"
BTN_PLAY = "Запуск"
STATUS_START = ""

FINISH_PLAY = lambda rpts: f"Завершено \n{rpts} повтор(ов)"
WORK_PLAY_STATUS = lambda rpts,cmds: f"Осталось \n{rpts} повтор(ов)\n{cmds} действий"
REMAIN_REPTS = lambda cmds: f"{len(cmds)}\n повтор(ов)"
REMAIN_CMDS = lambda cmds: f"Осталось {len(cmds)}\n команд"

SAVE_PATH = "Папка\n сохранения"
BTN_DIR = "Выбрать"
ASK_DIR_TITLE = "Выберить папку для сохранения файла экшена"
ASK_FILE_TITLE = "Выберить файл экшена"

