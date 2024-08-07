import curses, os

class twoColumn:
	def __init__ (self, stdscr):
		self.stdscr = stdscr
		self.height, self.width = self.stdscr.getmaxyx()
		self.col_width = self.width // 2

		self.tags = []
		self.directories = []
		self.files = []

		self.init_windows() 

	def init_tags (self):
		pass

	def load_contents (self):
		pass

	def init_windows (self):
		self.left_win = curses.newwin(self.height, self.col_width, 0, 0)
		self.right_win = curses.newwin(self.height, self.col_width, 0, self.col_width)
		self.left_win.box()
		self.right_win.box()


	def draw_windows (self):
		self.left_win.clear()
		self.right_win.clear()
		self.left_win.box()
		self.right_win.box()

	def handle_key (self):
		pass

	def mainloop (self):
		pass