from subprocess import Popen
import time
from threading import Thread
from os import system
import colorama

PROGRAM_TO_OPEN = "start.bat" # default starter file
PROGRAM_TO_CLOSE = "FXServer.exe" # default if you are using this for FiveM servers

TIME_TO_CLOSE = "06:00"

colorama.init(convert=True)


def watch():
    print(f"{colorama.Fore.LIGHTYELLOW_EX}Waiting for restart time{colorama.Fore.RESET}")
    while str(time.strftime("%R")) != TIME_TO_CLOSE:
        time.sleep(2)
    
    Popen(["taskkill", "/IM", PROGRAM_TO_CLOSE, "/F"], shell=True)
    system(f"start {PROGRAM_TO_OPEN}")
    print(f"{colorama.Fore.GREEN}Restarting server\n{colorama.Fore.LIGHTYELLOW_EX}Waiting 1 minute.{colorama.Fore.RESET}")
    time.sleep(60)
    watch()

Thread(target=watch).start()
