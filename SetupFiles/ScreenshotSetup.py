import pyautogui
import os


#directorypath
directoryPath = os.path.abspath(os.path.join(os.path.dirname( __file__ )))

input ("Press Enter after positioning mouse cursor in the top left section")

initialX,initialY = pyautogui.position()

input ("Press Enter after positioning mouse cursor in the bottom right section")
finalX, finalY = pyautogui.position()

print (initialX)
print (finalX)

directoryPath = directoryPath + "\printscreen.py"

with open (directoryPath, "r") as file:
	data = file.readlines()

#four-integer tuple of the left, top, width, and height of the region
data[7] = f'myScreenshot = pyautogui.screenshot(region=({initialX},{initialY}, {finalX-initialX}, {finalY-initialY}))\n'

with open (directoryPath, 'w') as file:
	file.writelines(data)
