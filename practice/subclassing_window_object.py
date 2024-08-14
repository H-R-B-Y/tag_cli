#! /usr/bin/python3

import curses

class my_window:
	mywindows = []

	@classmethod
	def sort_windows (cls):
		cls.mywindows.sort(key = lambda x: x.order)

	def __init__ (self, nlines, ncols, starty, startx, order = 0):
		self.win = curses.newwin(nlines, ncols, starty, startx)
		
		self.refresh = self.win.refresh
		self.clear = self.win.clear
	
		self.order = order
		self.drawable = []

		my_window.mywindows.append(self)

	def add_text(self, y, x, text):
		self.drawable.append([y,x,text])

	def draw_me (self):
		self.clear()
		self.win.box()
		for x in self.drawable:
			self.addstr(x[0], x[1], x[2])
		self.refresh()

	def __getattr__(self, name):
		# Delegate attribute access to the window object
		return getattr(self.win, name)



def main (stdscr):

	stdscr.clear()
	curses.cbreak()
	curses.noecho()
	height, width = stdscr.getmaxyx()

	overlap_top = my_window((height//2)+5, width, 0, 0, 1)
	overlap_top.add_text(1,1, "Top Text")

	overlap_bot = my_window(((height//2)+5), width, (height//2)-5, 0, 0)
	overlap_bot.add_text(1,1, "Bottom Text")

	overlap_left = my_window(height, ((width//2)+5), 0, 0, 2)
	overlap_left.add_text(height-2, 1, "Left Text")

	overlap_right =  my_window(height, ((width//2)+5), 0, (width//2)-5, 3)
	overlap_right.add_text(1, (((width//2)+4)-len("Right Text")), "Right Text")

	for x in my_window.mywindows: x.draw_me()
	stdscr.refresh()
	while True:
		my_window.sort_windows()
		for x in my_window.mywindows: x.draw_me()	
		stdscr.refresh()
		x = stdscr.getch()
		if (x == ord("w")):
			overlap_bot.order = 3
			overlap_top.order = 2
			overlap_left.order = 1
			overlap_right.order = 0
		elif (x == ord("s")):
			overlap_top.order = 3
			overlap_bot.order = 2
			overlap_left.order = 1
			overlap_right.order = 0
		elif (x == ord("a")):
			overlap_top.order = 0
			overlap_bot.order = 1
			overlap_left.order = 2
			overlap_right.order = 3
		elif (x == ord("d")):
			overlap_top.order = 0
			overlap_bot.order = 1
			overlap_left.order = 2
			overlap_right.order = 3
		elif (x == ord("q")):
			exit()

curses.wrapper(main)