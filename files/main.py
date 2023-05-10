from Lexer import *
from Parser import *

def main():
    string_input = "loh = 7\n hol = 5 + 6\n loh = hol"
    obj = Lexer(string_input)
    tokens = obj.Tokenize()
    print(tokens)
    parser = Parser(tokens)
    statement = parser.parse()

    print(variables)
main()

