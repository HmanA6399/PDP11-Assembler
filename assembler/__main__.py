import click
import sys

import stores
from tokenizer import Tokenizer
from pdp_parser import Parser
from io_lib import IO
from word_counter import WordCounter

def wordize(lines):
    """
    Parse and tokenize lines
    """
    parser      = Parser()
    tokenizer   = Tokenizer()
    word_ctr    = WordCounter()
    words = []
    for l in lines :
        if (l.rstrip()) :
            statement = parser.parseSentence(l, int(word_ctr))
            token_lists = tokenizer.tokenizeStatement(statement, int(word_ctr))
            for l in token_lists :
                if len(l) > 0 :
                    words.append(l)
                    word_ctr += 1
    return words

@click.group()
@click.version_option('1.0.0')
def main():
    pass

# Main Command
@main.command()
@click.argument('in_file', required=True)
@click.argument('out_file', required=True)
def compile(**kwargs):
    # Initialize IO Manager
    io_man      = IO()
    
    # Read the given file into lines
    lines = io_man.readFileIntoLines(kwargs.get("in_file"))

    # Lines to words
    words = wordize(lines)

    # Stringify word tokens into lines
    out_lines = [''.join([str(token) for token in word[::-1]]) + '\n' for word in words ]

    # Write to file
    io_man.writeLineToFile(kwargs.get("out_file"), out_lines)

    # Close the open files
    io_man.closeOpenFiles()

    pass

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("PDP11 Assembler")
    main()