from unittest
from Calculadora import Calculadora

class TestCalculadora(unitTest.TestCase):
	def test_suma_2_mas_2(self):
		calc=Calculadora()
		self.asserrEquals(4,calc.suma(2,2))
	def test_suma_2_mas_4(self):
		calc=Calculadora()
		self.asserrEquals(6,calc.suma(2,4))

if __name__ =='__main__':
	unittest.main()