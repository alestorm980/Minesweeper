class Cell:
	"""
	Cell class
	"""
	def __init__(self,pos_x,pos_y):

		self.active=True
		#has mine
		self.value="-"
		self.has_mine=False
		#location
		self.pos_x=pos_x
		self.pos_y=pos_y

	def __str__(self):
		if self.active:
			return self.value
		else:
			return "."			

	def set_has_mine(self,has_mine):
		self.has_mine=has_mine
		if self.has_mine:
			self.value="*"
		else:
			self.value="-"			

	def get_value(self):
		return self.value

	def values(self,game):
		if not self.has_mine:
			neigbor_mines=0
			for i in range(-1,2):
				for j in range(-1,2):
						if self.pos_x+i>=0 and self.pos_y+j>=0 and self.pos_x+i<game.get_height() and self.pos_y+j<game.get_width():
							if game.get_board()[self.pos_x+i][self.pos_y+j].get_value()=="*":
								if game.get_board()[self.pos_x+i][self.pos_y+j]!=self:
									neigbor_mines+=1
			if neigbor_mines!=0:
				self.value=str(neigbor_mines)

