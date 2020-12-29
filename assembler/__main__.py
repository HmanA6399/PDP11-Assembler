import stores
from tokenizer import Tokenizer
from pdp_parser import Parser
from io_lib import IO
from word_counter import WordCounter

# Initialize services
io_man      = IO()

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


if (__name__ == "__main__") :

    # Read the given file into lines
    lines = io_man.readFileIntoLines("in.asm")

    # Lines to words
    words = wordize(lines)

    # Stringify word tokens into lines
    out_lines = [''.join([str(token) for token in word[::-1]]) + '\n' for word in words ]

    # Write to file
    io_man.writeLineToFile("out.mem", out_lines)

    # Close the open files
    io_man.closeOpenFiles()