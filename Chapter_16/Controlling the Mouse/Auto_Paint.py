import pyautogui

pyautogui.click()  # to put paint in focus
distance = 200

while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)  # move right
    distance -= 25
    pyautogui.dragRel(0, distance, duration=0.1)  # move down
    distance -= 25
    pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
    distance -= 25
    pyautogui.dragRel(0, -distance, duration=0.1)  # move up

# dragRel for dragging and cliking at the same time
# !!! TO STOP THE PROGRAM, DRAG THE MOUSE TO THE TOP LEFT !!!

"""
To check the position of mouse and the color you are:
-Find python 3.8 from cmd

import pyautogui
pyautogui.displayMousePosition()
"""