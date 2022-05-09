from ui.View import View as ui
from model.Cafe import Cafe


if __name__ == '__main__':
    mainloop = True
    # Crear los espacios en memoria para los objetos
    cafe = None
    tables = []

    while mainloop:
        userOption = ui.menu()

        # CREATE
        if userOption == 1:
            table = ui.create()
            tables.append(table)


        # READ
        elif userOption == 2:
            cafe = Cafe(tables)
            ui.read(cafe)

        # UPDATE
        elif userOption == 3:
            ui.update()

        # DELETE
        elif userOption == 4:
            ui.delete()

        # EXIT
        elif userOption == 0:
            mainloop = False