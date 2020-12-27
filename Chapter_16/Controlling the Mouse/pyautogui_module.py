import pyautogui

print(pyautogui.size())  # size of the screen

width, height = pyautogui.size()

print(width, height)
print(pyautogui.position())  # the current position of the mouse

# pyautogui.moveTo(10, 10)  # move the cursor to...
# pyautogui.moveTo(10, 10, duration=2)  # for how long to be at the position
# pyautogui.moveRel(200, 0, duration=2)  # move the mouse from the current position to 200 at right in 2 seconds

print(pyautogui.position())  # get the position of mouse (in this case help)
pyautogui.click(691, 23)   # click on help button
# pyautogui.middleClick()  middle click
# pyautogui.rightClick() right click
# pyautogui.click()  click on the current mouse position

