#! /usr/bin/python3

import curses

def main(stdscr):
	# Clear screen
	stdscr.clear()

	# Set cbreak mode (no buffering) and noecho mode (don't display typed characters)
	curses.cbreak()
	curses.noecho()

	# Set up the screen for capturing input
	stdscr.addstr(0, 0, "Press any key. Press 'q' to exit.")

	while True:
		# Get the next character from the keyboard input
		ch = stdscr.getch()

		# If the character is 'q', exit the loop
		if ch == ord('q'):
			break

		# Display the raw key code at the top left of the screen
		stdscr.addstr(1, 0, f"Raw key code: {ch}")
		stdscr.refresh()

# Initialize curses and call the main function
curses.wrapper(main)
