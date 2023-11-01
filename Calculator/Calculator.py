import math

class Calculator:

    @staticmethod
    def calculation(first_operand: int, second_operand: int, operator: str):
        result = None

        match operator:
            case '+':
                result = first_operand + second_operand
            case '-':
                result = first_operand - second_operand
            case '*':
                result = first_operand * second_operand
            case '/':
                if second_operand != 0:
                    result = first_operand / second_operand
                else:
                    raise ArithmeticError("Division by zero is not possible")
            case _:
                raise ValueError(f"Unexpected value operator: + {operator}")

        return result

    @staticmethod
    def squareRootExtraction(num: float):

        if num < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        elif not isinstance(num, int):
            raise ValueError("you can only extract the root from an integer")
        elif math.sqrt(num) % 1 != 0:
            raise ValueError("the root values can only be integers")
        elif num == 0 :
            raise ValueError("Cannot calculate square root at 0")
        else:
            return math.sqrt(num)

    @staticmethod
    def calculating_discount(purchaseAmount: float, discountAmount: int):

            if purchaseAmount <= 0:
                raise ArithmeticError("Видимо у вас нет скидочки...")
            if discountAmount <= 0:
                raise ArithmeticError("Купите же что-то")
            if purchaseAmount > 1:
                raise ArithmeticError("скидка не может быть больше 100 процентов..., введите скидку от 0 до 1")

            return discountAmount - (purchaseAmount * discountAmount)




# c = Calculator()
# print(c.calculation(5, 5, '-'))
# print(c.squareRootExtraction(25))
# print(c.calculatingDiscount(1.1, 30))
# print(c.calculatingDiscount(1.1, 0))
