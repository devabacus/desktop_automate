import time
from core.record.main_rec import ActionRecorder


def main():
        
    ActionRecorder()

    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()