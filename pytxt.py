import sys

#  storing stdin in the var buffy and then spliting it by spaces

buffy = sys.stdin.read()
buffy = buffy.split(' ')


#  this function will capitalize everything in buffy join it together. And print
#  it out


def capAll():
    result = [x.upper() for x in buffy if x != '']
    result = ' '.join(result)
    print result


#  this function will lower everything in buffy and then join it together and
#  print the result


def lowAll():
    result = [x.lower() for x in buffy if x != '']
    result = ' '.join(result)
    print result


#  this will capitalize the specified letter (via numerical position or
#  specific letter via char) in each
#  word in buffy and print it out


def capLetter(n):
        if isinstance(n, (int, long)):
            n = n - 1
            m = n + 1
            result = [x[:n] + x[n].upper() + x[m:] for x in buffy if x != '' and len(x) > m]
            result = ' '.join(result)
            print result
        else:
            result = [x.upper().replace(n.lower(), n.upper()) for x in buffy if x != '']
            result = ' '.join(result)
            print result


#  this will lowercase the specified letter (via numerical position or specific
#  letter via char) in each
#  work in buffy and print it out


def lowLetter(n):
    if isinstance(n, (int, long)):
        n = n - 1
        m = n + 1
        result = [x[:n] + x[n].lower() + x[m:] for x in buffy if x != '' and len(x) > m]
        result = ' '.join(result)
        print result
    else:
        result = [x.replace(n.upper(), n.lower()) for x in buffy if x != '']
        result = ' '.join(result)
        print result


#  could parse text and grab any file paths in the text


def findPaths():
    paths = [x for x in buffy if x[0] == '/']
    paths = ' '.join(paths)
    print paths
findPaths()
