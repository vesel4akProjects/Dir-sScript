from pyautogui import write , press
import os
from time import  sleep
import psutil

def get_scan():
    os.system("start cmd")


    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == "cmd.exe":

            sleep(3)
            write("color 2")
            press("enter")
            sleep(1)
            write("dir /s")
            press("enter")

if __name__ == "__main__":
    get_scan()
