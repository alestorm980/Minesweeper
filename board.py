import random
from cell import Cell
class Board:
	"""
		Class Board:
		Contain a Cell array and some methods to change the board status
	"""
	def __init__(self,height,width,n_mines):
		#game options
		self.height=height
		self.width=width
		self.n_mines=n_mines

		#initial functions
		self.fill_board()
		self.random_mines()
		self.count_neighbors()

		#array of marks
		self.marks=[]
		# does the game end?
		self.end=False

	def get_height(self):
		return self.height

	def get_end(self):
		return self.end

	def get_width(self):
		return self.width

	def get_board(self):
		return self.board

	# for testing 
	def fixed_mines(self,mines):
		self.mines=	mines
		for mine in self.mines:
			i=(mine-1)/self.width
			j=(mine-1)%self.width
			self.board[i][j].set_has_mine(True)

	def random_mines(self):	
		# create n_mines random mines in a h*w board
		self.mines=[random.randint(1,self.height*self.width) for x in range(0,self.n_mines) ]
		for mine in self.mines:
			#get the position from the actual mine
			i=(mine-1)/self.width
			j=(mine-1)%self.width
			# set has mine true
			self.board[i][j].set_has_mine(True)

	# fill the board  with cell objects
	def fill_board(self):
		self.board=[]
		for x in range(0,self.height):
			row=[]
			for y in range(0,self.width):
				cell=Cell(x,y)
				row.append(cell)
			self.board.append(row)

	# count neigbours for each cell
	def count_neighbors(self):
		for x in range(0,self.height):
			for y in range(0,self.width):			
				self.board[x][y].count_neighbor_mines(self)

	# init function for uncover cell		
	def init_uncover_cell(self,x,y):
		#validate index
		if(x>=0 and y>=0 and x<self.height and y<self.width):
			if(self.is_a_loser(x,y)):
				self.loser()
			else:				
				self.uncover_cell(x,y)
				self.print_board()
		else:
			print "Position is not valid"	

	def uncover_cell(self,x,y):
		if(x>=0 and y>=0 and x<self.height and y<self.width):
			if not self.board[x][y].get_state():
				#change state when uncover
				self.board[x][y].set_state(True)
				#change mark when uncover
				self.board[x][y].set_mark(False)
				#only iterate over cells with 0 neighbors
				if(self.board[x][y].get_neighbor_mines()==0):
					for i in range(-1,2):
						for j in range(-1,2):
							if x+i>=0 and y+j>=0 and x+i<self.height and y+j<self.width:
								#uncover recursively for each neighbor
								self.uncover_cell(x+i,y+j)			
	def init_mark_cell(self,i,j):
		if self.board[i][j].get_state():
			print "Cell is not valid"
		else:
			self.mark_cell(i,j)			

	# mark cell with P and change mark attribute
	def mark_cell(self,i,j):
		#validate index
		if(i>=0 and j>=0 and i<self.height and j<self.width):
			if not self.board[i][j].get_state():
				if not self.board[i][j].get_mark():
					#set has mark as true
					self.board[i][j].set_mark(True)
					#add current mark to marks array
					self.marks.append(self.board[i][j])
					self.print_board()
					print "The cell ("+str(i)+","+str(j)+") has been marked"
					if self.is_a_winner():
						self.congratulation()

				else:
					#set has mark as true
					self.board[i][j].set_mark(False)
					#delete mark
					self.marks.remove(self.board[i][j])
					self.print_board()
					print "The cell ("+str(i)+","+str(j)+") has been unmarked"
		else:
			print "Position is not valid"

	def is_a_winner(self):
		if len(self.marks) == len(self.mines):
			for mark in self.marks:
				if mark.get_value()!="*":
					return False
			return True
		else:
			return False

	def is_a_loser(self,x,y):
		if self.board[x][y].get_value()=="*":
			self.end=True
			return True
		else:
			return False			

	def congratulation(self):
		self.end=True
		print "=)"
		print "CONGRATULATION YOU WIN!!!!"
		print ""

	def loser(self):
		for mine in self.mines:
			i=(mine-1)/self.width
			j=(mine-1)%self.width
			self.board[i][j].set_state(True)
		self.print_board()			
		print "=("
		print "Sorry, you lost!!"
		print "Try again"
		print ""

	#print board method
	def print_board(self):
		print ""
		print "Board                                  Table of position"
		print ""
		i=0
		j=0
		for x in range(0,self.height):
			line=""
			line_aux=""
			j=0
			for y in range(0,self.width):
				line+=str(self.board[x][y])+" "
				line_aux+="("+str(i)+","+str(j)+") "
				j+=1
			print line+"         "+line_aux
			i+=1			
		print ""
		print "--------------------------"	
		print ""