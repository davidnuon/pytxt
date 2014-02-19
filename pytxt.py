import sys


buffy = sys.stdin.read()
buffy = buffy.split(' ')


def capAll():
    result = [x.upper() for x in buffy if x != '']
    result = ' '.join(result)
    print result


def lowAll():
    result = [x.lower() for x in buffy if x != '']
    result = ' '.join(result)
    print result


def capLetter(n):
    n = n - 1
    m = n + 1
    result = [x[:n] + x[n].upper() + x[m:] for x in buffy if x != '' and len(x) > m]
    result = ' '.join(result)
    print result


def lowLetter(n):
    n = n - 1
    m = n + 1
    result = [x[:n] + x[n].lower() + x[m:] for x in buffy if x != '' and len(x) > m]
    result = ' '.join(result)
    print result
