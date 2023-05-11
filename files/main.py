from Lexer import *
from Parser import *

def main():
    string_input = " #Алгебра " \
                   "пер = 2 ^ 2 " \
                   " пердва = 1" \
                   " Доколе ( 1 , 10 )" \
                   " { " \
                   "    пер = пер + 1 " \
                   "    пердва = пердва + 3 + пер " \
                   " } " \
                   " пертри = 3 " \
                   " Доколе ( 1 , 5 )" \
                   "    пертри = пертри ^ 2 "
    obj = Lexer(string_input)
    tokens = obj.Tokenize()
    print(tokens)
    parser = Parser(tokens)

    program = parser.parse()
    program.execute()
    # for stmt in program:
    #     if stmt is not None:
    #         stmt.execute()

    print(variables)


main()

