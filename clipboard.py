import subprocess
import sys


os = sys.platform

def getClip():
    #  gets the operating system
    if os == 'darwin':
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        buffy = p.stdout.read()
        return buffy
    elif os == 'linux2':
        p = subprocess.Popen(['xsel --clipboard --output'], stdout=subprocess.PIPE)
        buffy = p.stdout.read()
        return buffy
    elif os == 'win32':
        pass


def setClip()
    #  gets the operating system
    if os == 'darwin':
        p = subprocess.Popen(['pbcopy'], stdout=subprocess.PIPE)
        buffy = p.stdout.read()
        return buffy
    elif os == 'linux2':
        p = subprocess.Popen(['xsel --clipboard --input'], stdout=subprocess.PIPE)
        buffy = p.stdout.read()
        return buffy

