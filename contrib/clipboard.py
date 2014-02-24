import subprocess
import sys
from Tkinter import Tk

os = sys.platform

def getClip():
    #  gets the operating system
    if os == 'darwin':
        try:
            p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
            buffy = p.stdout.read()
            return buffy
        except OSError:
            print 'Xcode is not installed'
    elif os == 'linux2':
        try:
            p = subprocess.Popen(['xsel --clipboard --output'], stdout=subprocess.PIPE)
            buffy = p.stdout.read()
            return buffy
        except OSError:
            print 'xsel must be installed'
    elif os == 'win32':
        p = Tk()
        buffy = p.selection_get(selection='CLIPBOARD')
        return buffy


def setClip(data):
    #  gets the operating system
    if os == 'darwin':
        try:
            p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            p.stdin.write(data)
            p.stdin.close()
        except OSError:
            print 'Xcode is not installed'
    elif os == 'linux2':
        try:
            p = subprocess.Popen(['xsel --clipboard --input'], stdin=subprocess.PIPE)
            p.stdin.write(data)
            p.stdin.close()
        except OSError:
            print 'xsel must be installed'
    elif os == 'win32':
        p = Tk()
        p.clipboard_clear()
        p.clipboard_append(data)
        p.destroy()
