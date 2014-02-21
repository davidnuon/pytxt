import subprocess


#  methods for piping from the clipboard

def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    buffy = p.stdout.read()
    return buffy


def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

#  this function will capitalize everything in buffy join it together. And print
#  it out


def capAll():
    buffy = getClipboardData()
    buffy = buffy.split(' ')
    result = [x.upper() for x in buffy if x != '']
    result = ' '.join(result)
    result = setClipboardData(result)
    return result


#  this function will lower everything in buffy and then join it together and
#  print the result


def lowAll():
    buffy = getClipboardData()
    buffy = buffy.split(' ')
    result = [x.lower() for x in buffy if x != '']
    result = ' '.join(result)
    result = setClipboardData(result)
    return result

#  this will capitalize the specified letter (via numerical position or
#  specific letter via char) in each
#  word in buffy and print it out


def capLetter(n):
    buffy = getClipboardData()
    buffy = buffy.split(' ')
    if isinstance(n, (int, long)):
        n = n - 1
        m = n + 1
        result = [x[:n] + x[n].upper() + x[m:] for x in buffy if x != '' and len(x) > m]
        result = ' '.join(result)
        result = setClipboardData(result)
        return result
    else:
        result = [x.upper().replace(n.lower(), n.upper()) for x in buffy if x != '']
        result = ' '.join(result)
        result = setClipboardData(result)
        return result

#  this will lowercase the specified letter (via numerical position or specific
#  letter via char) in each
#  work in buffy and print it out


def lowLetter(n):
    buffy = getClipboardData()
    buffy = buffy.split(' ')
    if isinstance(n, (int, long)):
        n = n - 1
        m = n + 1
        result = [x[:n] + x[n].lower() + x[m:] for x in buffy if x != '' and len(x) > m]
        result = ' '.join(result)
        result = setClipboardData(result)
        return result
    else:
        result = [x.replace(n.upper(), n.lower()) for x in buffy if x != '']
        result = ' '.join(result)
        result = setClipboardData(result)
        return result

#  could parse text and grab any file paths in the text


def findPaths():
    buffy = getClipboardData()
    buffy = buffy.split()
    paths = [x for x in buffy if x[0] == '/']
    paths = ' '.join(paths)
    paths = setClipboardData(paths)
    return paths
