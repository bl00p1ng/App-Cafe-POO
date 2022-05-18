from venv import create


class View:
    def menu():
        print("""
╔═╗┌─┐┌─┐┌─┐  ╔═╗┌┬┐┌┬┐┬┌┐┌
║  ├─┤├┤ ├┤   ╠═╣ │││││││││
╚═╝┴ ┴└  └─┘  ╩ ╩─┴┘┴ ┴┴┘└┘

1 --> Crear mesa y añadir productos
2 --> Mostar mesas
3 --> Actualizar mesa
4 --> Borrar mesa
0 --> Salir

        """)
        userOption = int(input('--> Ingresa una opción: '))
        return userOption


    def create():
        """Formulario para crear una mesa con sus respectivos productos"""

        print('********** CREAR MESA **********')
        tableName = input('--> Ingresa el nombre de la mesa (ej: Mesa 01): ')

        # Obtener los productos del usuario, pedirá que se registren productos hasta que
        # makerOther sea False
        products = []
        makeOther = True

        while makeOther:
            productName = input('--> Ingresa el nombre del producto: ')
            price = int(input('--> Ingresa el precio del producto: '))
            products.append([productName, price])

            makeOther = int(input('--> Quieres añadir otro producto (1 - SI | 2 - NO): '))
            makeOther = True if makeOther == 1 else False

        return (tableName, products)


    # READ
    def read(cafe):
        """Mostrar las mesas con sus respectivos productos"""
        print('********** MOSTRAR MESAS **********')
        cafe.showTables()


    # UPDATE
    def update(tableNames):
        """Actualizar los datos de una mesa especifica"""
        print('********** ACTUALIZAR MESA **********')        

        print(':: Nombres de las mesas')
        for tableName in tableNames:
            print(f'* {tableName}')
        
        # Obtener la mesa a actualizar
        tableToUpdate = input('--> Ingresa el nombre de la mesa a actualizar: ')

        # Obtener los productos nuevos de la mesa
        newProducts = []
        makeOther = True

        print(':: Ingresa los productos actualizados\n')
        while makeOther:
            productName = input('--> Ingresa el nombre del producto: ')
            price = int(input('--> Ingresa el precio del producto: '))
            newProducts.append([productName, price])

            makeOther = int(input('--> Quieres añadir otro producto (1 - SI | 2 - NO): '))
            makeOther = True if makeOther == 1 else False
        
        return (tableToUpdate, newProducts)


    # DELETE
    def delete(tableNames):
        """Obtiene el nombre de la mesa a eliminar"""
        print('********** ELIMINAR MESA **********')

        print(':: Nombres de las mesas')
        for tableName in tableNames:
            print(f'* {tableName}')

        # Obtener la mesa a actualizar
        tableToDelete = input('--> Ingresa el nombre de la mesa a eliminar: ')        
        
        return tableToDelete
