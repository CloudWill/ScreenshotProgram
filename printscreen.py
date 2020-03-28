import pyautogui
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H%M%S")
pathName = f'./screenshots/{now}.png'

#four-integer tuple of the left, top, width, and height of the region
myScreenshot = pyautogui.screenshot(region=(587,546, 528, 185))
myScreenshot.save(pathName)
