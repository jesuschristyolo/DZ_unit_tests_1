from Shop import Shop
from Product import Product
from unittest import TestCase, main

#Напишите тесты, чтобы проверить, что магазин хранит верный список продуктов(правильное количество продуктов, верное содержимое корзины).

class ShopTest(TestCase):

    def setUp(self):
        self.shop = Shop()
        self.product = Product()

        p1 = Product()
        p1.set_cost(50)
        p2 = Product()
        p2.set_cost(100)
        p3 = Product()
        p3.set_cost(20)
        p4 = Product()
        p4.set_cost(1000)

        self.shop.set_products([p1, p2, p3, p4])

    def test_product_list(self):

        p1 = Product()
        p1.set_cost(50)
        p2 = Product()
        p2.set_cost(100)
        p3 = Product()
        p3.set_cost(20)
        p4 = Product()
        p4.set_cost(1000)

        self.shop.set_products([p1, p2, p3, p4])
        self.assertEqual(len(self.shop.get_products()), 4)
        self.assertEqual(self.shop.get_products(), [p1, p2, p3, p4])

        with self.assertRaises(ValueError) as a:
            self.shop.set_products([p1, p2, p3, 15])

        self.assertEqual("Не все объекты списка являются объектами класса Product!", a.exception.args[0])


    def test_get_most_expensive_product(self):
        self.assertEqual(self.shop.get_most_expensive_product(), 1000)

    def test_sort_products_by_price(self):
        self.assertEqual(self.shop.sort_products_by_price(), [self.shop.get_products()[2], #self.cost = 20
                                                              self.shop.get_products()[0], #self.cost = 50
                                                              self.shop.get_products()[1], #self.cost = 100
                                                              self.shop.get_products()[3]]) #self.cost = 1000






if __name__ == '__main__':
    main()
