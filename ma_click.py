# import win32api
import time
import random
import keyboard
from pykeyboard import *
from pymouse import *

import _thread

# def click(self, x, y, button = 1, n = 1):
#     """Click a mouse button n times on a given x, y.
#     Button is defined as 1 = left, 2 = right, 3 = middle.
#     """

#     for i in range(n):
#         self.press(x, y, button)
#         self.release(x, y, button)

global_trigger = True
def autoClick():
    global global_trigger
    m = PyMouse()
    k = PyKeyboard()

    interval = 0.1
    offset = 20

    x, y = 1525, 663
    while global_trigger:
        time.sleep(interval)
        print(m.position())

        lrand = random.randint(-offset, offset)
        rrand = random.randint(-offset, offset)
        print("lrand = ", lrand)
        print("rrand = ", rrand)
        print("trigger: ", global_trigger)
        print("===============")
        m.click(x = x + lrand, 
                y = y + rrand, 
                button = 1, 
                n = 1)
        # m.click(x=m.position()[0], y=m.position()[1], button=1, n=1)

def listenKeyboard(key = '`'):
    global global_trigger
    keyboard.wait(hotkey = key)
    global_trigger = False
    print("listenKeyboard()")

def mainTask():
    _thread.start_new_thread( autoClick, () )
    _thread.start_new_thread( listenKeyboard, () )

# run
mainTask()
keyboard.wait('shift + `')
# listenKeyboard()






