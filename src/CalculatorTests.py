import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setup(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 4)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(580, 459), 1039)
        self.assertEqual(self.calculator.result, 1039)


if __name__ == '__main__':
    unittest.main()
