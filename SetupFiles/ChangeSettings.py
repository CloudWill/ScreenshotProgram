import os
import json


def reset_default():
    settingsPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    screenShotPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Screenshots'))

    defaultSettings = {"ScreenshotLocation": f"{screenShotPath}",
                       "Shortcut": "^J",
                       "x1": "0",
                       "y1": "0",
                       "x2": "1919",
                       "y2": "1079"
                       }

    with open(settingsPath + '\\Settings.txt', 'w') as f:
        json.dump(defaultSettings, f)


def change_shortcut_key(path, sc):
    path = path + "\\SetupAhkFile.py"
    # reads the file
    with open(path, "r") as file:
        data = file.readlines()
    data[6] = f'\tss = "{sc}"\n'
    # writes to the file
    with open(path, 'w') as file:
        file.writelines(data)
