class cell:

	def __init__(self,mine,pos_x,pos_y):

		self.active=False
		#has mine
		self.mine=mine
		#location
		self.pos_x=pos_x
		self.pos_y=pos_y
	
	def value(self,board):
		if self.mine:
			self.value="*"
		else:
			neigbor_mines=0
				for i in range(-1,2):
					for j in range(-1,2):
						if board[i][j]!=self:
							if pos_x+i>=0 and pos_y+i>=0 or pos_x+i<board.get_height() and pos_y+i<board.get_width() and board.get_board()[pos_x+1][pos_y+1]=="*":
									neigbor_mines+=1
			if neigbor_mines==0
				self.value="-"
			else:
				self.value=str(neigbor_mines)
				

