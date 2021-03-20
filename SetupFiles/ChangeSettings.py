import os
import json


def ChangePrintScreen(path, ssLoc):
    path = path + "\\Printscreen.py"
    # reads the file
    with open(path, "r") as file:
        data = file.readlines()

    if ssLoc == '/':
        print('changing to default')
        data[8] = f'screenshotPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ),' \
                  f' \'..\', \'Screenshots\'))\n'
    else:
        print('changing to new path')
        data[8] = f'screenshotPath = "{ssLoc}"\n'

    # writes to the file
    with open(path, 'w') as file:
        file.writelines(data)


def ChangeShortcutKey(path, sc):
    path = path + "\\SetupAhkFile.py"
    # reads the file
    with open(path, "r") as file:
        data = file.readlines()
    print(f'changing to {data[4]}')
    data[4] = f'ss = "{sc}"\n'
    # writes to the file
    with open(path, 'w') as file:
        file.writelines(data)


SettingsPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

with open(SettingsPath + '\\Settings.txt', 'r') as f:
    data = json.load(f, strict=False)

SettingsPath = SettingsPath + "\\SetupFiles"
ChangePrintScreen(SettingsPath, data["ScreenshotLocation"])
ChangeShortcutKey(SettingsPath, data["Shortcut"])
