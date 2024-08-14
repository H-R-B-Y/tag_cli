#! /usr/bin/python3

"""
YEAH THEY CAN WOOOHOOOOO!!!!!!!!!
"""

import curses

def main(stdscr):
	# Clear screen
	stdscr.clear()

	# Set cbreak mode (no buffering) and noecho mode (don't display typed characters)
	curses.cbreak()
	curses.noecho()

	height, width = stdscr.getmaxyx()

	# Set up the screen for capturing input
	top_left_win = curses.newwin(height//2, width//2, 0, width//2)
	top_right_win = curses.newwin(height//2, width//2, 0, 0)
	bot_left_win = curses.newwin(height//2, width//2, height//2, width//2)
	bot_right_win = curses.newwin(height//2, width//2, height//2, 0)
	middle_win = curses.newwin(height//2, width//2, height//4, width//4)
	wins = [bot_right_win, bot_left_win, top_right_win, top_left_win, middle_win]
	[x.box() for x in wins]
	middle_win.addstr("q: Quit\n")
	middle_win.addstr("p: Toggle Help")
	
	stdscr.refresh()
	[x.refresh() for x in wins]
	while True:
		x = stdscr.getch()
		if (x == ord("p") and middle_win in wins):
			wins.remove(middle_win)
		elif (x == ord("p")):
			wins.append(middle_win)
		elif (x == ord("q")):
			exit()
		[x.clear() for x in wins]
		[x.box() for x in wins]
		if (middle_win in wins):
			middle_win.addstr("q: Quit\n")
			middle_win.addstr("p: Toggle Help")
		[x.refresh() for x in wins]



curses.wrapper(main)