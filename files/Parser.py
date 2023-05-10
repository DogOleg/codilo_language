from NumberExpression import *
from OperationExpression import *
from UnaryExpression import *
from AssigmentStatement import *
from VariableExpression import *
from BlockStatement import *
from ForStatement import *
#from .variableExpression import *
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.size = len(tokens)

    def parse(self):
        result = []
        while(not self.match("EOF")):
            result.append(self.statement())
        return result

    def block(self):

        #self.consume("LBRACE")
        self.pos+=1
        while (not self.match("RBRACE")):
            block = addStatement(self.statement())
        return block
    def statement(self):
        if self.match("FOR"):
            return self.forStatement()
        return self.assigmentStatement()

    def assigmentStatement(self):
        current = self.get(0)
        if (self.match("WORD") and list(self.get(0))[0] == "EQ"):

            variable = current["WORD"]
            self.pos += 1
            #self.consume("EQ")

            resultToVariable = self.Expression()
            result_Variable = AssigmentStatement(variable, resultToVariable)
            result_Variable.execute()
            return result_Variable

        raise Exception ("Unknown Statement")

    #def consume(self):
     #   current = self.get(0)

    def statementOrBlock(self):
        if list(self.get(0))[0] == "LBRACE":
            return self.block()
        else:
            return self.statement()

    def Expression(self):
        return self.additive()

    def additive(self):
        result = self.multiplicative()

        while (True):
            if (self.match("PLUS")):
                result = OperationExpression("+", result, self.multiplicative())
                continue
            if (self.match("MINUS")):
                result = OperationExpression("-", result, self.multiplicative())
                continue
            break

        return result

    def multiplicative(self):
        result = self.unary()

        while(True):
            if(self.match("MULTY")):
                result = OperationExpression("*", result, self.unary())
                continue
            if (self.match("DEL")):
                result = OperationExpression("/", result, self.unary())
                continue
            break

        return result

    def unary(self):
        if (self.match("MINUS")):
            return UnaryExpression("-", self.primary())
        return self.primary()

    def primary(self):
        current = self.get(0)
        if (self.match("NUMBER")):
            numberExrpession = NumberExpression(float(current["NUMBER"]))
            return numberExrpession
        if(self.match("LPAREN")):
            result = self.Expression()
            self.match("RPAREN")
            return result
        if(self.match("WORD")):
            variablesexpression = VariableExpression(current["WORD"])
            return variablesexpression
        raise Exception('unknown expression')

    def forStatement(self):
        list(self.get(0))[0] == "LPARREN"
        self.pos += 1
        start = self.primary()
        list(self.get(0))[0] == "COMMA"
        self.pos += 1
        finish = self.primary()
        list(self.get(0))[0] == "RPARREN"
        self.pos += 1
        block = self.statementOrBlock()

        statement = ForStatement(int(start.eval()), int(finish.eval()), block)
        return statement


    def match(self, type):
        current = self.get(0)
        if(type != list(current)[0]):
            return False
        self.pos += 1
        return True



    def get(self, relativePosition):
        position = self.pos + relativePosition
        if(position >= self.size):
            return {"EOF": ""}
        return self.tokens[position]