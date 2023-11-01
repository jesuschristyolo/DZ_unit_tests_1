import unittest
from unittest import TestCase, main
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculation(self):
        self.assertEqual(self.calculator.calculation(5,5,'-'),0)
        self.assertEqual(self.calculator.calculation(0,1,'/'),0)
        self.assertEqual(self.calculator.calculation(-5,10,'*'),-50)
        self.assertEqual(self.calculator.calculation(-50,-10,'+'),-60)

        with self.assertRaises(ValueError) as a:
            self.calculator.calculation(1, 1, 'erte')

        self.assertEqual(f"Unexpected value operator: + {'erte'}", a.exception.args[0])


        with self.assertRaises(ValueError) as a:
            self.calculator.calculation(1, 1, 'erte')

        self.assertEqual(f"Unexpected value operator: + {'erte'}", a.exception.args[0])


        with self.assertRaises(ArithmeticError) as a:
            self.calculator.calculation(1, 0, '/')

        self.assertEqual("Division by zero is not possible", a.exception.args[0])


    def test_calculating_discount(self):
        self.assertEqual(self.calculator.calculating_discount(1.0, 50,), 0)
        self.assertEqual(self.calculator.calculating_discount(0.75, 500,), 125)
        self.assertEqual(self.calculator.calculating_discount(0.1, 500,), 450)

        with self.assertRaises(ArithmeticError) as a:
            self.calculator.calculating_discount(-1, 500)

        self.assertEqual("Видимо у вас нет скидочки...", a.exception.args[0])

        with self.assertRaises(ArithmeticError) as a:
            self.calculator.calculating_discount(0.72, -500)

        self.assertEqual("Купите же что-то", a.exception.args[0])

        with self.assertRaises(ArithmeticError) as a:
            self.calculator.calculating_discount(1.1, 500)

        self.assertEqual("скидка не может быть больше 100 процентов..., введите скидку от 0 до 1", a.exception.args[0])







if __name__ == '__main__':
    unittest.main()