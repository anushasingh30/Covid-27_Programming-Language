import argparse

from antlr4 import *

from covid27.antlr.covid27Lexer import covid27Lexer
from covid27.antlr.covid27Parser import covid27Parser
from covid27.compiler.covid27Intermediate import InterimCodeGenerator
from covid27.executor.covid27Runtime import Runtime

def compiler(filepath, output):
    input = FileStream(filepath)
    lexer = covid27Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = covid27Parser(stream)

    tree = parser.program()
    if '.icovid27' not in output:
        output = output + '.icovid27'
    listener = InterimCodeGenerator(output)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

def run(filepath):
    runtime = Runtime(filepath)
    runtime.execute()

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
