import argparse

from antlr4 import *

def compiler(filepath, output):
    raise NotImplementedError()

def run(filepath):
    raise NotImplementedError()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', help="Compile the given file to object code",
                        action='store_true')
    parser.add_argument('--r',  help="Run the given object code file",
                        action='store_true')
    parser.add_argument('--i', type=str, default='a.covid27',
                        help="The file to be ran or to be executed")
    parser.add_argument('--o', type=str, default='a.icovid27',
                        help="The output object file.")
    args = parser.parse_args()

    if args.c:
        compiler(args.i, args.o)
    if args.r:
        run(args.i)
