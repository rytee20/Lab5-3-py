import unittest
import datetime

from Accessories import Accessories
from Clothes import Clothes
from Product import toFixed
from Shoes import Shoes


class Tests(unittest.TestCase):
    def test_total_price_1(self):
        product = Clothes(48, "shirt", "O'stin", "man", "White shirt", 20, 15, 0.7, 1999, 45)
        self.assertEqual(product.total_price(10), toFixed(1799.1, 2))

    def test_total_price_2(self):
        product = Clothes(46, "shirt", "GloriaJeans", "woman", "Hello Kitty shirt", 20, 15, 1.2, 1499, 100)
        if datetime.datetime.now().day == 8 and datetime.datetime.now().mounth == 3:
            self.assertEqual(product.total_price(10), toFixed(1049.1, 2))
        else:
            self.assertEqual(product.total_price(10), toFixed(1349.1, 2))

    def test_total_price_3(self):
        product = Clothes(48, "outerwear", "Mango", "woman", "Coat", 20, 15, 10, 7999, 3)
        if datetime.datetime.now().day == 8 and datetime.datetime.now().mounth == 3:
            self.assertEqual(product.total_price(10), toFixed(5599.3, 2))
        elif datetime.datetime.now().month == 8:
            self.assertEqual(product.total_price(10), toFixed(6399.2, 2))
        else:
            self.assertEqual(product.total_price(10), toFixed(7199.1, 2))

    def test_total_price_4(self):
        product = Shoes(37, "high-heels", "Nike", "woman", "Pink heels with bow", 25, 17, 10, 2499, 98)
        self.assertEqual(product.total_price(10), toFixed(2249.1, 2))

    def test_total_price_5(self):
        product = Accessories("belt", "GloriaJeans", "woman", "Jast a belt", 10, 5, 5, 999, 100)
        if datetime.datetime.now().day == 8:
            self.assertEqual(product.total_price(10), toFixed(699.3, 2))
        else:
            self.assertEqual(product.total_price(10), toFixed(899.1, 2))

    def test_fit_in_a_box_1(self):
        product = Clothes(48, "shirt", "O'stin", "man", "White shirt", 20, 15, 0.7, 1999, 45)
        self.assertEqual(product.fit_in_a_box(20, 15, 1), 1)

    def test_fit_in_a_box_2(self):
        product = Clothes(48, "shirt", "O'stin", "man", "White shirt", 20, 15, 0.7, 1999, 45)
        self.assertEqual(product.fit_in_a_box(20, 30, 7), 20)
