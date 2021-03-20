import os
import sys
import json
import subprocess
from pathlib import Path
import ScreenshotSetup
import ChangeSettings
import SetupAhk


def set_settings():
    settingsPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    with open(settingsPath + '\\Settings.txt', 'r') as f:
        data = json.load(f, strict=False)
    return data


def run_option(jsonData, option):
    directoryPath = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    if option == "1":
        ScreenshotSetup.change_screenshot_size(jsonData)
    elif option == "2":
        reload_program(directoryPath)
    elif option == "3":
        ChangeSettings.reset_default()
        reload_program(directoryPath)
    elif option == "4":
        ScreenshotSetup.print_screen(jsonData["ScreenshotLocation"],jsonData)
    elif option == "5":
        start_ahk(directoryPath)
    elif option == "0":
        print("Exiting")
    else:
        print("Invalid input. Please try again")
    print(f"\n\n* * * done * * * \n\n")


def reload_program(directoryPath):
    #refreshes with new data
    jsonData = set_settings()
    sc = jsonData["Shortcut"]
    # make the directory if it does not exist
    Path(jsonData["ScreenshotLocation"]).mkdir(parents=True, exist_ok=True)
    SetupAhk.create_ahk_file(directoryPath,sc)
    start_ahk(directoryPath)

def start_ahk(directoryPath):
    resetAhk = directoryPath + "\\StartAhk.bat"
    subprocess.call([rf'{resetAhk}'])

# to see if it's user run or script run
jsonData = set_settings()
n = len(sys.argv)
if n == 1:
    var = "-1"
    while var != "0":
        var = input(f"Please enter a number and press the enter key: \n"
                    f" 1 - Change the screenshot size \n"
                    f" 2 - Update Settings (screenshot location or shortcut) \n"
                    f" 3 - Reset All Settings \n"
                    f" 4 - Take a screenshot \n"
                    f" 5 - Start Ahk\n"
                    f" 0 - exit \n ")
        run_option(jsonData, var)

    # run explict option
else:
    run_option(jsonData, sys.argv[1])

exit(0)
