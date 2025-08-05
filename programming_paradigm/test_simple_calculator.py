import unittest
from simple_calculator import SimpleCalculator

calculator = SimpleCalculator()

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1,2),3)
    def test_subtract(self):
        self.assertEqual(calculator.subtract(2,1),1)
    def text_multiplication(self):
        self.assertEqual(calculator.multiply(2,2),4)
    def test_division(self):
        self.assertEqual(calculator.divide(4,2),2)
        self.assertEqual(calculator.divide(2,0),None)