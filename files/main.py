from Lexer import *
from Parser import *

def main():
    string_input = "loh = 0 @  ( 1 , 10 ) loh = loh + 1"
    obj = Lexer(string_input)
    tokens = obj.Tokenize()
    print(tokens)
    parser = Parser(tokens)
    statement = parser.parse()
    for stmt in statement:
        if stmt is not None:
            stmt.execute()
    print(variables)


main()

