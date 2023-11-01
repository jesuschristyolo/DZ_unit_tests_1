from Product import Product
class Shop:

    __products = []

    def get_products(self):
        return self.__products

    def set_products(self, products):
        if all(isinstance(x, Product) for x in products):
            self.__products = products
        else:
            raise ValueError("Не все объекты списка являются объектами класса Product!")

    def sort_products_by_price(self):
        return sorted(self.__products, key=lambda x: x)

    def get_most_expensive_product(self):
        return max([i.get_cost() for i in self.__products])




# p = Product()
# p.set_cost(12)
# p3 = Product()
# p3.set_cost(20)
# p1 = Product()
# p1.set_cost(15)
# s = Shop()
# s.set_products([p,p3, p1])
# print(s.get_products(), 'df')
# print(s.get_most_expensive_product())
# print(s.sort_products_by_price(), 'r')
# print(s.__dict__)
# for i in s.sort_products_by_price():
#     print(i.__dict__)

