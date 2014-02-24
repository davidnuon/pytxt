from contrib.clipboard import getClip, setClip

if getClip() == '':
    print 'There is nothing in the clipboard!'
else:
    pass

#  capital method does .upper() on clipboard


def capAll():
    buffy = getClip()
    result = buffy.upper()
    result = setClip(result)
    return result


#  this function will lower everything in buffy and then join it together and
#  print the result


def lowAll():
    buffy = getClip()
    result = buffy.lower()
    result = setClip(result)
    return result

#  this will capitalize the specified letter (via numerical position or
#  specific letter via char) in each
#  word in buffy and print it out


def capLetter(n):
    buffy = getClip()
    buffy = buffy.split(' ')
    if isinstance(n, (int, long)):
        n = n - 1
        m = n + 1
        result = [x[:n] + x[n].upper() + x[m:] for x in buffy if x != '' and len(x) > m]
        result = ' '.join(result)
        result = setClip(result)
        return result
    else:
        result = [x.replace(n.lower(), n.upper()) for x in buffy if x != '']
        result = ' '.join(result)
        result = setClip(result)
        return result

#  this will lowercase the specified letter (via numerical position or specific
#  letter via char) in each
#  work in buffy and print it out


def lowLetter(n):
    buffy = getClip()
    buffy = buffy.split(' ')
    if isinstance(n, (int, long)):
        n = n - 1
        m = n + 1
        result = [x[:n] + x[n].lower() + x[m:] for x in buffy if x != '' and len(x) > m]
        result = ' '.join(result)
        result = setClip(result)
        return result
    else:
        result = [x.replace(n.upper(), n.lower()) for x in buffy if x != '']
        result = ' '.join(result)
        result = setClip(result)
        return result

#  could parse text and grab any file paths in the text


def findPaths():
    buffy = getClip()
    buffy = buffy.split()
    paths = [x for x in buffy if x[0] == '/']
    paths = ' '.join(paths)
    if paths != '':
        paths = setClip(paths)
        return paths
    else:
        print 'There are no paths in this text!'
