from pyautogui import write , press
import os
from time import  sleep

def get_scan():
    os.system("start cmd")
    sleep(1)
    write("color 2")
    press("enter")
    sleep(1)
    write("dir /s")
    press("enter")



if __name__ == "__main__":
    get_scan()
