from Lexer import *
from Parser import *

def main():
    string_input = "loh = 0 @  ( 1 , 10 ) { loh = loh + 1 }"
    obj = Lexer(string_input)
    tokens = obj.Tokenize()
    print(tokens)
    parser = Parser(tokens)

    program = parser.parse()
    #program.execute()
    for stmt in program:
        if stmt is not None:
            stmt.execute()

    print(variables)


main()

