import os


def create_ahk_file(directoryPath, shortcutKey):
    f = open(directoryPath + "\\AutoHotKeysSettings.ahk", "w")

    # .ahk file for autohotkey
    f.write(f'{shortcutKey}:: \n run, python.exe "{directoryPath}\\Main.py" 4')

    f.close()
