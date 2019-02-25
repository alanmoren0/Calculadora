import unittest
'#from unittest import testCase'
from Calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    def test_suma_2_mas_2(self):
        calc = Calculadora()
        self.assertEquals(4, calc.suma(2, 2))

    def test_suma_2_mas_4(self):
        calc = Calculadora()
        self.assertEquals(6, calc.suma(2, 4))


if __name__ == '__main__':
    unittest.main()
