class BlockStatement:
    def __init__(self, statements):
        statements = self.statements

    def add(self, statement):
        self.statements.add(statement)

    def execute(self):
        for i in range(len(self.statements)):
            self.statements[i].execute()