class Cell:
	"""
	Cell class
	each cell has 
	"""
	def __init__(self,pos_x,pos_y):
		#initial state
		self.state=False
		#initial value
		self.value="-"

		#has mine?
		self.has_mine=False
		#has mark?
		self.mark=False
		#neighbor_mines
		self.neighbor_mines=0

		#location
		self.pos_x=pos_x
		self.pos_y=pos_y

	def get_value(self):
		return self.value

	def get_state(self):
		return self.state

	def get_mark(self):
		return self.mark
	def get_neighbor_mines(self):
		return self.neighbor_mines
	def set_mark(self,mark):
		self.mark=mark

	def set_value(self,value):
		self.value=value		
		
	def set_state(self,state):
		self.state=state

	def set_has_mine(self,has_mine):
		self.has_mine=has_mine
		if self.has_mine:
			self.value="*"
		else:
			self.value="-"			

	def __str__(self):
		if self.mark:
			return "P"
		elif self.state:
			return self.value
		else:
			return "."	

	def count_neighbor_mines(self,game):
		if not self.has_mine:
			neighbor_mines=0
			for i in range(-1,2):
				for j in range(-1,2):
						if self.pos_x+i>=0 and self.pos_y+j>=0 and self.pos_x+i<game.get_height() and self.pos_y+j<game.get_width():
							if game.get_board()[self.pos_x+i][self.pos_y+j].get_value()=="*":
								if game.get_board()[self.pos_x+i][self.pos_y+j]!=self:
									neighbor_mines+=1
			if neighbor_mines!=0:
				self.value=str(neighbor_mines)
				self.neighbor_mines=neighbor_mines

