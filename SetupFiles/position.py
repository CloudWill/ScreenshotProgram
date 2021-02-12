import pyautogui
import os

input ("Press Enter after positioning mouse cursor in the top left section")

initialX,initialY = pyautogui.position()

input ("Press Enter after positioning mouse cursor in the bottom right section")
finalX, finalY = pyautogui.position()

print (initialX)
print (finalX)

with open ("printscreen.py", "r") as file:
	data = file.readlines()

#four-integer tuple of the left, top, width, and height of the region
data[7] = f'myScreenshot = pyautogui.screenshot(region=({initialX},{initialY}, {finalX-initialX}, {finalY-initialY}))\n'

with open ("printscreen.py", 'w') as file:
	file.writelines(data)

#setups the ahk	script
with open ("../2-hotkeys.ahk", "r") as file:
	data = file.readlines()

currentDir = os.getcwd()

data[3] = f'python "{currentDir}\printscreen.py"\n'

with open ("../2-hotkeys.ahk", "w") as file:
	data = file.writelines(data)
