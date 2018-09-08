from board import Board

class Game:
	"""
		Class Game
		Contains one board object and methods usefull for play
	"""
	def __init__(self):
		self.init_parse()
		self.board=Board(self.height,self.width,self.n_mines)
	def usage(self):
		print "Please enter the height, width and number of mines that you want"

	#parse input data for each game
	def parse_game(self,line):
		split_line=line.split(' ')
		try:
			i=int(split_line[0])
			j=int(split_line[1])
			option=split_line[2]

			if option =="U":
				self.board.uncover_cell(i,j)
			elif option =="M":
				self.board.mark_cell(i,j)
			else:
				print "Invalid Option"

			self.board.print_board()
		except ValueError:
			print "Input error"
			self.usage()

	#parse initial input height width and mines
	def init_parse(self):
		line=raw_input("Please enter the height, width and number of mines that you want \n")
		split_line=line.split(' ')
		try:
			self.height=int(split_line[0])
			self.width=int(split_line[1])
			self.n_mines=int(split_line[2])
		except:
			print "Input Arguments"
			self.usage()
			exit(0)

	def start_game(self):
		a=1

def main():
	print "-------------------------------------------"
	print "Welcome to the Minesweeper Game!!!"
	print "-------------------------------------------"
	print ""
	g=Game()



if __name__=="__main__":
	main()