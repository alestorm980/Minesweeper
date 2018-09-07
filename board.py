import numpy as np
import random
from cell import Cell
class Game:
	"""
		Game Class
	"""
	def __init__(self,height,width,n_mines):
		self.height=height
		self.width=width
		self.n_mines=n_mines
		self.fill_board()
		self.random_mines()
		self.count_mines()

	def random_mines(self):	
		mines=[random.randint(1,self.height*self.width) for x in range(0,self.n_mines) ]
		for mine in mines:
			i=(mine-1)/self.width
			j=(mine-1)%self.width
			self.board[i][j].set_has_mine(True)

	def get_height(self):
		return self.height

	def get_width(self):
		return self.width

	def get_board(self):
		return self.board

	def fill_board(self):
		self.board=[]
		for x in range(0,self.height):
			row=[]
			for y in range(0,self.width):
				cell=Cell(x,y)
				row.append(cell)
			self.board.append(row)

	def count_mines(self):
		for x in range(0,self.height):
			for y in range(0,self.width):			
				self.board[x][y].values(self)

	def print_board(self):
		for x in range(0,self.height):
			line=""
			for y in range(0,self.width):
				line+=str(self.board[x][y])+" "
			print line
a=Game(6,10,5)
a.print_board()


