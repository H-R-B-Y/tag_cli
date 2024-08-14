#! /usr/bin/python3

"""
YEAH THEY CAN WOOOHOOOOO!!!!!!!!!
"""

import curses

def main(stdscr):
	stdscr.clear()

	curses.cbreak()
	curses.noecho()

	height, width = stdscr.getmaxyx()
	
	stdscr.refresh()
	
	while True:
		x = stdscr.getch()



curses.wrapper(main)