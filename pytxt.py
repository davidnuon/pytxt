""" Pytxt.

Usage:
    pytxt.py capAll
    pytxt.py lowAll
    pytxt.py capLetter (<letter> | <position>)
    pytxt.py lowLetter (<letter> | <position>)
    pytxt.py findPaths
    pytxt.py (-h | --help)
    pytxt.py --version

Options:
    -h --help   Show this screen.
    --version   Show version.

"""

from docopt import docopt
import functions


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Pytxt 0.0.1')

    capAll = arguments.get('capAll')
    lowAll = arguments.get('lowAll')
    capLetter = arguments.get('<letter>')
    lowLetter = arguments.get('<letter>')
    paths = arguments.get('findPaths')

    if capLetter:
        functions.capLetter(capLetter)
    elif lowLetter:
        functions.lowLetter(lowLetter)
    elif capAll:
        functions.capAll()
    elif lowAll:
        functions.lowAll()
    elif paths:
        functions.findPaths()
    else:
        print 'Invalid'
