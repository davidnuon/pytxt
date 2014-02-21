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

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Pytxt 0.0.1')
    print(arguments)
