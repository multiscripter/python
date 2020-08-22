import unittest # Unit testing framework for Python.
import unittest.mock # Mock object library.
# https://docs.python.org/3/library/unittest.html#module-unittest
# Source code: https://github.com/python/cpython/tree/3.8/Lib/unittest/__init__.py

from mymath import *

class TestMymath(unittest.TestCase):

	def testAddReturnSuccess(self):
		self.assertEqual(add(10, 20), 30)
		self.assertTrue(add(10, 20) == 30)

	def testAddThrowsTypeError(self):
		# assertRaises(exception, callable, *args, **kwds)
		# assertRaises(exception, *, msg=None)
		self.assertRaises(TypeError, add, 100, 'str')

	def testDivideSuccess(self):
		self.assertTrue(divide(4, 2), 2.0)

	def testDivideThrowsZeroDivisionError(self):
		self.assertRaises(ZeroDivisionError, divide, 100, 0)

unittest.main()