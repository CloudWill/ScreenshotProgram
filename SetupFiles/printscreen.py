import pyautogui
from datetime import datetime
from pathlib import Path
import os
##start
#do not change as position.py relies on line 7
#four-integer tuple of the left, top, width, and height of the region
myScreenshot = pyautogui.screenshot(region=(158,81, 1451, 585))
screenshotPath = "D:/OneDrive/Sorted/Programming/Python/PrintScreen/test"
##end

now = datetime.now().strftime("%Y-%m-%d %H%M%S")


# #make the directory if it does not exist
Path(screenshotPath).mkdir(parents=True, exist_ok=True)

pathName = f'{screenshotPath}/{now}.png'

myScreenshot.save(pathName)
