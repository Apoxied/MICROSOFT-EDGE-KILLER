import psutil
import time

#Bye Bye
def prevent_msedge():
    while True:
        time.sleep(1)
        for proc in psutil.process_iter():
            if proc.name() == "msedge.exe":
                proc.kill()

prevent_msedge()
