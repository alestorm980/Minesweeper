import numpy as np
import random
from cell import Cell
class Board:
	"""
		Game Board
	"""
	def __init__(self,height,width,n_mines):
		self.height=height
		self.width=width
		self.n_mines=n_mines
		self.fill_board()
		self.random_mines()
		self.count_neighbors()

	def get_height(self):
		return self.height

	def get_width(self):
		return self.width

	def get_board(self):
		return self.board

	def random_mines(self):	
		self.mines=[random.randint(1,self.height*self.width) for x in range(0,self.n_mines) ]
		for mine in self.mines:
			i=(mine-1)/self.width
			j=(mine-1)%self.width
			self.board[i][j].set_has_mine(True)

	def fill_board(self):
		self.board=[]
		for x in range(0,self.height):
			row=[]
			for y in range(0,self.width):
				cell=Cell(x,y)
				row.append(cell)
			self.board.append(row)

	def count_neighbors(self):
		for x in range(0,self.height):
			for y in range(0,self.width):			
				self.board[x][y].neighbor_mines(self)

	def uncover_cell(self,i,j):
		if(i>=0 and j>=0 and i<self.height and j<self.width):
			if not self.board[i][j].get_state():
				self.board[i][j].set_state(True)
				self.print_board()
		else:
			print "Position not valid"

	def mark_cell(self,i,j):
		if(i>=0 and j>=0 and i<self.height and j<self.width):

			if not self.board[i][j].get_state():

				if not self.board[i][j].get_mark():
					self.board[i][j].set_mark(True)
					self.print_board()
					print "The cell ("+str(i)+","+str(j)+") has been marked"
				else:
					self.board[i][j].set_mark(False)
					self.print_board()
					print "The cell ("+str(i)+","+str(j)+") has been unmarked"
		else:
			print "Position not valid"			


	def print_board(self):
		print ""
		for x in range(0,self.height):
			line=""
			for y in range(0,self.width):
				line+=str(self.board[x][y])+" "
			print line
		print ""
		print "--------------------------"	
		print ""		
			
a=Board(6,10,2)
a.print_board()

a.mark_cell(2,3)
a.mark_cell(2,4)
