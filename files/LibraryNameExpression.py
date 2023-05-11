class LibraryNameExpression:
    def __init__(self, statement):
        self.statement = statement
    def execute(self):
            self.statement.execute()