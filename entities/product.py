from valuesobjects.money import Money

class Product:
    def __init__(self, name: str, price: Money):
        self.name = name
        self.price = price