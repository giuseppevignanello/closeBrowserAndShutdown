import pyautogui
import time
import subprocess

#set the timer 
waiting_time = 2700
time.sleep(waiting_time)
# close the browser 
with pyautogui.hold('ctrl'):
        pyautogui.keyDown('shift')
        pyautogui.press('w')

# wait for the browser and cmd closing 
time.sleep(5)

#shutdown 
subprocess.run(["shutdown", "/s", "/t", "0"])