from ui.View import View as ui
from model.Cafe import Cafe
from model.Table import Table


if __name__ == '__main__':
    mainloop = True
    # Crear los espacios en memoria para los objetos
    cafe = None
    tables = []

    while mainloop:
        userOption = ui.menu()

        # CREATE
        if userOption == 1:
            # Obtener los datos para crear una mesa
            tableName, products = ui.create()
            # Crear una instancia de mesa
            table = Table(tableName, products)
            # Coleccionar las mesas creadas
            tables.append(table)
            # Crear una instancia de Cafe con las mesas coleccionadas
            cafe = Cafe(tables)

        # READ
        elif userOption == 2:
            ui.read(cafe)

        # UPDATE
        elif userOption == 3:
            # Obtener los nombres de las mesas
            tableNames = cafe.getTableNames()
            # Obtener la mesa a actualizar y sus productos nuevos
            tableToUpdate, newProducts = ui.update(tableNames)
            cafe.updateTable(tableToUpdate, newProducts)

        # DELETE
        elif userOption == 4:
            ui.delete()

        # EXIT
        elif userOption == 0:
            mainloop = False