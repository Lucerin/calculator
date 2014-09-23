#!usr/bin/env python
from Calculator import Calculator
import unittest
class TestCalcultor(unittest.TestCase):
	def test_suma_2_mas_2(self):
		self.cal=Calculator()
		self.assertEqual(4, self.cal.suma(2,2))

	def test_suma_1_mas_4(self):
		self.cal=Calculator()
		self.assertEqual(5, self.cal.suma(1,4))
		
	def test_suma_12_mas_9(self):
		self.cal=Calculator()
		self.assertEqual(21, self.cal.suma(12,9))		

	def test_resta_2_menos_2(self):
		self.cal=Calculator()
		self.assertEqual(0, self.cal.resta(2,2))

	def test_resta_2_menos_1(self):
		self.cal=Calculator()
		self.assertEqual(1, self.cal.resta(2,1))

	def test_resta_19_menos_2(self):
		self.cal=Calculator()
		self.assertEqual(17, self.cal.resta(19,2))
	def test_multi_2_por_2(self):
		self.cal=Calculator()
		self.assertEqual(4, self.cal.multi(2,2))
		
	def test_multi_2_por_1(self):
		self.cal=Calculator()
		self.assertEqual(2, self.cal.multi(2,1))	
	def test_multi_2_por_0(self):
		self.cal=Calculator()
		self.assertEqual(0, self.cal.multi(2,0))		
	def test_division_2_entre_5(self):
		self.cal=Calculator()
		self.assertEqual(10, self.cal.division(50,5))
	def test_division_2_entre_2(self):
		self.cal=Calculator()
		self.assertEqual(1, self.cal.division(2,2))

	def test_division_12_entre_6(self):
		self.cal=Calculator()
		self.assertEqual(2, self.cal.division(12,6))

if __name__== '__main__':
	unittest.main()

