from Variables import *

class VariableExpression:
    def init(self, name):
        self.name = name


    def eval(self):
        return variables.get(self.name)