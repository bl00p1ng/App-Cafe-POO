from model.Table import Table


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


        table = Table(tableName, products)


    # READ
    def read():
        pass


    # UPDATE
    def update():
        pass


    # DELETE
    def delete():
        pass