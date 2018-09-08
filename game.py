from board import Board
import sys
# change recursion limit
sys.setrecursionlimit(100000)
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
	def play(self):
		line=raw_input("Please enter the position and option\n")
		split_line=line.split(' ')
		if len(split_line)!=3:
			return -1
		try:
			i=int(split_line[0])
			j=int(split_line[1])
			option=split_line[2]

			if option =="U":
				self.board.init_uncover_cell(i,j)
			elif option =="M":
				self.board.init_mark_cell(i,j)
			else:
				print "Invalid Option"

			#self.board.print_board()
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
			if(self.n_mines>self.height*self.width):
				print "The number of mines must be lower than the cells"
				exit(0)
		except:
			print "Error!!!"
			self.usage()
			exit(0)

	def print_g(self):
		self.board.print_board()
	
	def is_end(self):
		return self.board.end



def main():
	print "-------------------------------------------"
	print "Welcome to the Minesweeper Game!!!"
	print "-------------------------------------------"
	print ""
	salir=False
	while not salir:
		game=Game()
		print "Creating new game..."
		game.print_g()
		while(not game.is_end()):
			game.play()
		option=raw_input("Play Again 1-Yes Other-No \n")
		if option != "1":
			salir=True




if __name__=="__main__":
	main()