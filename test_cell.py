from cell import Cell
import unittest

class TestBoard(unittest.TestCase):

	def test_set_has_mine(self):
		c=Cell(4,6)
		c.set_has_mine(True)
		self.assertEqual(c.get_value(),"*")

	def test_str_mark(self):
		c=Cell(4,6)
		c.set_mark(True)
		self.assertEqual(str(c),"P")