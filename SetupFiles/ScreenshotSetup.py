import pyautogui
import os
from datetime import datetime
import json


def change_screenshot_size(jsonData):
    input("Press Enter after positioning mouse cursor in the top left section")
    x1, y1 = pyautogui.position()

    input("Press Enter after positioning mouse cursor in the bottom right section")
    x2, y2 = pyautogui.position()

    print(f'x1 is {x1} x2 is {y1} x2 is {x2} y2 is {y2}')

    jsonData["x1"] = x1
    jsonData["y1"] = y1
    jsonData["x2"] = x2 - x1
    jsonData["y2"] = y2 - y1

    settingsPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    with open(settingsPath + '\\Settings.txt', 'w') as f:
        json.dump(jsonData, f)


def print_screen(ssDir,jsonData):
    x1 = jsonData["x1"]
    y1 = jsonData["y1"]
    x2 = jsonData["x2"]
    y2 = jsonData["y2"]
    myScreenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
    now = datetime.now().strftime("%Y-%m-%d %H%M%S")
    pathName = f'{ssDir}\\{now}.png'
    myScreenshot.save(pathName)
