class Cafe:
    def __init__(self, tables=[]):
        self.__tables = []

        for table in tables:
            self.__tables.append(table)


    # Methods
    def showTables(self):
        for table in self.__tables:
            table.showTable()


    # Getters
    def getTables(self):
        return self.__tables


    # Setters
    def setTables(self, index, newTable):
        self.__tables[index] = newTable
