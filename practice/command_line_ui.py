#! /usr/bin/python3

import curses

def main(stdscr):
	# Clear screen
	stdscr.clear()
	
	# Get screen dimensions
	max_y, max_x = stdscr.getmaxyx()
	
	# Create a window for the menu
	menu_win = curses.newwin(max_y, max_x, 0, 0)
	menu_win.keypad(True)
	curses.use_default_colors()
	
	# Menu items
	menu = ["Home", "Settings", "Quit"]
	current_row = 0
	
	while True:
		# Clear the menu window
		menu_win.clear()
		
		# Display menu items
		for idx, item in enumerate(menu):
			if idx == current_row:
				menu_win.attron(curses.color_pair(1))
				menu_win.addstr(idx, 0, item)
				menu_win.attroff(curses.color_pair(1))
			else:
				menu_win.addstr(idx, 0, item)
		
		# Refresh the window
		menu_win.refresh()
		
		# Get user input
		key = menu_win.getch()
		
		if key == curses.KEY_DOWN:
			current_row = (current_row + 1) % len(menu)
		elif key == curses.KEY_UP:
			current_row = (current_row - 1) % len(menu)
		elif key == curses.KEY_ENTER or key == 10:
			if menu[current_row] == "Quit":
				break
			else:
				menu_win.addstr(max_y - 1, 0, f"Selected {menu[current_row]}")
				menu_win.refresh()
				menu_win.getch()
	
curses.wrapper(main)