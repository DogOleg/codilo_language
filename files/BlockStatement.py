from Statement import *
class BlockStatement(Statement):
    statements = []
    # def __init__(self, statement):
    #     self.statements = statement

    def add(self, statement):
        self.statements.append(statement)

    def execute(self):
        super().execute()
        for i in range(len(self.statements)):
            self.statements[i].execute()


