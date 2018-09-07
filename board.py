import numpy as np
import random
from cell import Cell
class Board:
	"""
		Board Class
	"""
	def __init__(self,height,width,n_mines):
		self.height=height
		self.width=width
		self.n_mines=n_mines
		self.fill_board()
		self.random_mines()
		self.count_mines()

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

	def random_mines(self):
		current_mines=0
		while(current_mines<self.n_mines):
			mine=random.randint(1,self.height*self.width)
			i=(mine-1)/self.width
			j=(mine-1)%self.width
			if self.board[i][j].get_value()=="-":
				self.board[i][j].set_has_mine(True)
				current_mines+=1			

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
a=Board(6,10,5)
a.print_board()


