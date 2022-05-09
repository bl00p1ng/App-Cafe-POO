from ui.View import View as ui


if __name__ == '__main__':
    mainloop = True

    while mainloop:
        userOption = ui.menu()

        # CREATE
        if userOption == 1:
            ui.create()

        # READ
        elif userOption == 2:
            ui.read()

        # UPDATE
        elif userOption == 3:
            ui.update()

        # DELETE
        elif userOption == 4:
            ui.delete()

        # EXIT
        elif userOption == 0:
            mainloop = False