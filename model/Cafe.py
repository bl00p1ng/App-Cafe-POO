class Cafe:
    def __init__(self, tables=[]):
        self.__tables = []

        for table in tables:
            self.__tables.append(table)


    # Getters
    def getTables(self):
        return self.__tables


    # Setters
    def setTables(self, index, newTable):
        self.__tables[index] = newTable
