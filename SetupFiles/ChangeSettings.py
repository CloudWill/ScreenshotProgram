import os
import json

def ChangePrintScreen(path, ssLoc):
    #reads the file
    with open(path + "\\printscreen.py", "r") as file:
        data = file.readlines()

    if ssLoc == '/':
        print('changing to default')
        data[8] = f'screenshotPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ),' \
                  f' \'..\', \'screenshots\'))\n'
    else:
        print('changing to new path')
        data[8] = f'screenshotPath = "{ssLoc}"\n'

    #writes to the file
    with open(path + "\\printscreen.py", 'w') as file:
        file.writelines(data)

def ChangeShortcutKey(path, sc):
    # reads the file
    with open(path + "\\SetupAhkFile.py", "r") as file:
        data = file.readlines()
    print(f'changing to {data[4]}')
    data[4] = f'ss = "{sc}"\n'
    # writes to the file
    with open(path + "\\SetupAhkFile.py", 'w') as file:
        file.writelines(data)


print("starting")
SettingsPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

with open(SettingsPath + '\\Settings.txt', 'r') as f:
    data = json.load(f, strict=False)

SettingsPath = SettingsPath + "\\SetupFiles"
ChangePrintScreen(SettingsPath, data["ScreenshotLocation"])
ChangeShortcutKey(SettingsPath, data["Shortcut"])


print("ending")
