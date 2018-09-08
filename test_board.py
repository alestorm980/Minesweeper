from board import Board
import unittest

class TestBoard(unittest.TestCase):

	def test_is_a_winner(self):
		#test for winner
		height=6
		width=10
		b=Board(height,width,2)
		mines=[3,11,15,28]
		b.fixed_mines(mines)

		for mine in mines:
			i=(mine-1)/width
			j=(mine-1)%width
			b.init_mark_cell(i,j)

		self.assertTrue(b.is_a_winner())
		#test more marks than real mines
		b=Board(height,width,2)
		mines=[3,11,15,28]
		b.fixed_mines(mines)
		mines.append(56)
		for mine in mines:
			i=(mine-1)/width
			j=(mine-1)%width
			b.init_mark_cell(i,j)

		self.assertFalse(b.is_a_winner())

	def test_is_a_loser(self):
		height=6
		width=10
		b=Board(height,width,2)
		mines=[3,11,15,28]
		b.fixed_mines(mines)

		mine=mines[0]
		i=(mine-1)/width
		j=(mine-1)%width
		
		b.init_uncover_cell(i,j)

		self.assertTrue(b.is_a_loser(i,j))

					



