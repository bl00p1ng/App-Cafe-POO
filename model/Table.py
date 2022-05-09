from model.Product import Product


class Table:
    def __init__(self, tableName='Sin asignar', products=[]):
        self.__tableName = tableName
        self.__products = []

        for product in products:
            self.__products.append(Product(name=product[0], price=product[1]))


    # Methods
    def showTable(self):
        """Mostrar la información de la mesa"""
        print(f'***** {self.__tableName} *****')
        
        print('+----------+--------+')
        print('| Producto | Precio |')
        print('+----------+--------+')

        for product in self.__products:
            print(f"|{''.join(['-']) * (product.productLenght() + 5)}|")
            product.showProduct()
        print(f"+{''.join(['-']) * (product.productLenght() + 5)}+")


    # Getters
    def getTableName(self):
        return self.__tableName


    # Setters
    def setTableName(self, newtableName):
        self.__tableName = newtableName
