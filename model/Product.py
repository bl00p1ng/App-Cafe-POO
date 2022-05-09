class Product:
    def __init__(self, name='Sin nombre', price=0):
        self.__name = name
        self.__price = price


    # Methods
    def showProduct(self):
        """Mostrar producto"""
        print(f'| {self.__name} | {self.__price} |')


    def productLenght(self):
        """Retorna la longitud de la representación en Strings
        de las propiedades del objeto"""
        return len(self.__name) + len(str(self.__price))


    # Getters
    def getName(self):
        return self.__name


    def getPrice(self):
        return self.__price

    # Setters
    def setName(self, newName):
        self.__name = newName


    def setPrice(self, newPrice):
        self.__price = newPrice