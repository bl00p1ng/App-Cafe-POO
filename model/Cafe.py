class Cafe:
    def __init__(self, tables=[]):
        self.__tables = []

        for table in tables:
            self.__tables.append(table)


    # Methods
    def showTables(self):
        for table in self.__tables:
            table.showTable()


    def getTableNames(self):
        """Recorre las tablas seleccionadas y obtiene su nombre"""
        tableNames = []
        for table in self.__tables:
            tableNames.append(table.getTableName())
        return tableNames


    def updateTable(self, tableToUpdate, newProducts):
        """Toma los datos nuevos y los actualiza en las mesa correspondiente
            Recibe el nombre de la mesa a actualizar"""
        for table in self.__tables:
            if table.getTableName() == tableToUpdate:
                table.update(newProducts)


    # Getters
    def getTables(self):
        return self.__tables


    # Setters
    def setTables(self, index, newTable):
        self.__tables[index] = newTable
