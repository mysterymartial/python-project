import unittest
import calc


class Testcalc (unittest.Testcase):

	def test_add(self):
		result = calc.add(3,2)
		self.assertEqual(result, 5)





if __name__ == '__'main__:
	unittest.main()