class Product:

    __cost = 0
    __title = ""


    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def __lt__(self, other):
        return self.get_cost() < other.get_cost()


p = Product()
p.set_cost(12)
p1 = Product()
p.set_cost(14)
print(p < p1)

