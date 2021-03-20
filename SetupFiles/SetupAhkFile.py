import os

#do not change as ChangeSettings relies on these lines
##start
ss = "^u"
##end

directoryPath = os.path.abspath(os.path.join(os.path.dirname( __file__ )))

f = open(directoryPath+"\AutoHotKeysSettings.ahk", "w")

#.ahk file for autohotkey
f.write(f'{ss}:: \n run, python.exe "{directoryPath}\printscreen.py')

f.close()
