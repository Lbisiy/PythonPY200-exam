from main import Product
import unittest


class TestProduct(unittest.TestCase):
    """
    Тестирование Класса Продукт
    """

    def test_id(self):
        self.assertIsInstance(Product('Ivan', 500, 5).id, int)

    def test_name(self):
        self.assertRaises(TypeError, Product, 500, 500, 5)
        self.assertIsInstance(Product('Ivan', 500, 5).name, str)

    def test_price(self):
        self.assertRaises(TypeError, Product, 'Ivan', '500', 5)
        self.assertRaises(ValueError, Product, 'Ivan', 0, 5)
        self.assertIsInstance(Product('Ivan', 500, 5).price, int)
        self.assertIsInstance(Product('Ivan', 500.00, 5).price, float)

    def test_rating(self):
        self.assertRaises(TypeError, Product, 'Ivan', 500, '5')
        self.assertRaises(ValueError, Product, 'Ivan', 0, -5)
        self.assertIsInstance(Product('Ivan', 500, 5).rating, int)
        self.assertIsInstance(Product('Ivan', 500.00, 5.00).rating, float)


if __name__ == '__main__':
    unittest.main()
