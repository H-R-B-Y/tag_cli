#! /usr/bin/python3

import curses, os

# This needs to be documented better please!!!!!!!!!!!!

TAG_LOCATION = os.path.expanduser(os.environ["TAGS_DIR"]) + "/"
CLAMP = lambda x, min, max: (min if x < min else (max if x > max else x))
OUTPUTFILE = os.path.expanduser(os.environ["SCRIPT_DIR"]) + "/navto" # This hard coding needs to be removed at some point lacks portability
# installation script should populate the hard coded values with correct locations!


class twoColumn:

	class modes:
		_modes = [0, 1, 2]
		navigate = 0
		append = 1
		delete = 2


	def __init__ (self, stdscr):
		self.stdscr = stdscr
		self.height, self.width = self.stdscr.getmaxyx()
		self.col_width = self.width // 2

		curses.curs_set(0)
		self.stdscr.nodelay(0)  # Ensure blocking mode for getch
		self.stdscr.timeout(-1)
		curses.cbreak()  # Enable cbreak mode
		curses.noecho()
		self.stdscr.keypad(True)

		self.tags = []
		self.directories = []
		self.files = []

		self._mode = self.modes.navigate

		self.cursor = [0,0]
		self.cursor_swap = [0,0]

		self.kill_switch = False

		self.init_tags()
		self.init_colors()
		self.load_contents(self.tags[0])
		self.init_windows() 
		self.context_bar.attron(curses.color_pair(2))
		self.update_context_bar("n: new tag  |  del: delete a Tag or untag a file/folder  |  q: quit")
		self.context_bar.attroff(curses.color_pair(2))

	@property
	def mode (self):
		return self._mode

	@mode.setter
	def mode (self, newMode):
		assert newMode in self.modes._modes
		if (newMode == self.modes.append):
			curses.curs_set(1)
			curses.nocbreak()
			curses.echo()
			self.stdscr.keypad(False)
		elif (newMode == self.modes.navigate):
			curses.curs_set(0)
			curses.cbreak()
			curses.noecho()
			self.stdscr.keypad(True)
		elif (newMode == self.modes.delete):
			curses.curs_set(1)
			curses.nocbreak()
			curses.echo()
			self.stdscr.keypad(False)
		self._mode = newMode

	def init_colors(self):
			# Initialize the default color settings
			curses.start_color()
			curses.use_default_colors()
			curses.init_pair(1, curses.COLOR_RED, -1)    # Color 1: Red text
			curses.init_pair(2, curses.COLOR_GREEN, -1)  # Color 2: Green text
			curses.init_pair(3, curses.COLOR_YELLOW, -1) # Color 3: Yellow text
			curses.init_pair(4, curses.COLOR_BLUE, -1)   # Color 4: Blue text
			curses.init_pair(5, curses.COLOR_MAGENTA, -1) # Color 5: Magenta text
			curses.init_pair(6, curses.COLOR_CYAN, -1)   # Color 6: Cyan text
			curses.init_pair(7, curses.COLOR_WHITE, -1)  # Color 7: White text

	def init_tags (self):
		self.tags = next(os.walk(TAG_LOCATION))[1]

	def load_contents (self, tag):
		temp, self.directories, self.files = next(os.walk(TAG_LOCATION+tag))

	def init_windows (self):
		self.left_win = curses.newwin(self.height-1, self.col_width, 0, 0)
		self.right_win = curses.newwin(self.height-1, self.col_width, 0, self.col_width)
		self.context_bar = curses.newwin(1, self.width, self.height-1, 0)
		self.left_win.box()
		self.right_win.box()
		self.stdscr.refresh()

	def update_context_bar (self, text):
		self.context_bar.clear()
		self.context_bar.addstr(0,0, text)
		self.context_bar.refresh()

	# handle scrolling eventually
	def draw_windows (self):
		self.left_win.clear()
		self.right_win.clear()
		self.left_win.attron(curses.color_pair(5))
		self.left_win.box()
		self.left_win.addstr(0,0, "Tags")
		self.left_win.attroff(curses.color_pair(5))
		self.right_win.attron(curses.color_pair(6))
		self.right_win.box()
		self.right_win.addstr(0,0, "Files/Folders")
		self.right_win.attroff(curses.color_pair(6))
		pad = 1
		i = 0
		for tag in self.tags:
			self.left_win.attron(curses.color_pair(6) if not [i, 0] == self.cursor else curses.color_pair(4))
			self.left_win.addstr(pad+i, pad+0, tag + (" >"if ([i,0] == self.cursor_swap and self.cursor[1] == 1) else ""))
			self.left_win.attroff(curses.color_pair(6) if not [i, 0] == self.cursor else curses.color_pair(4))
			if ([i,0] == self.cursor):
				self.load_contents(tag)
			i += 1
		i = 0
		for directory in self.directories:
			self.right_win.attron(curses.color_pair(5) if not [i, 1] == self.cursor else curses.color_pair(4))
			self.right_win.addstr(pad+i, pad+0, directory + "/")
			self.right_win.attroff(curses.color_pair(5) if not [i, 1] == self.cursor else curses.color_pair(4))
			if ([i, 1] == self.cursor):
				p = os.path.realpath(TAG_LOCATION+self.tags[self.cursor_swap[0]]+"/"+directory+"/")+"/"
				self.update_context_bar(p)
			i += 1
		i += 1
		for file in self.files:
			self.right_win.attron(curses.color_pair(5) if not [i-1, 1] == self.cursor else curses.color_pair(4))
			self.right_win.addstr(pad+i, pad+0, file)
			self.right_win.attroff(curses.color_pair(5) if not [i-1, 1] == self.cursor else curses.color_pair(4))
			if ([i-1, 1] == self.cursor):
				p = os.path.dirname(os.path.realpath(TAG_LOCATION+self.tags[self.cursor_swap[0]]+"/"+file))+"/"
				self.update_context_bar(p)
			i += 1

		self.left_win.refresh()
		self.right_win.refresh()

	def navigation (self, direction):
		if (direction == curses.KEY_LEFT and self.cursor[1] != 0):
			self.cursor = self.cursor_swap
			self.update_context_bar("")
		elif (direction == curses.KEY_RIGHT and self.cursor[1] != 1 and (len(self.directories) + len(self.files)) != 0): # This can be used to implement sub directories later
			self.cursor_swap = self.cursor
			self.cursor = [0, 1]
		elif (direction == curses.KEY_UP and self.cursor[0] != 0):
			self.cursor[0] = CLAMP(self.cursor[0]-1, 0, ([len(self.tags), len(self.directories) + len(self.files)][self.cursor[1]])-1)
		elif (direction == curses.KEY_DOWN):
			self.cursor[0] = CLAMP(self.cursor[0]+1, 0, ([len(self.tags), len(self.directories) + len(self.files)][self.cursor[1]])-1)

	def enter_action (self):
		output = ""
		if (self.cursor[1] == 0):
			return self.navigation(curses.KEY_RIGHT)
		if (self.cursor[0] < len(self.directories)):
			output = TAG_LOCATION + self.tags[self.cursor_swap[0]] + "/" + self.directories[self.cursor[0]]
		elif (self.cursor[0] - len(self.directories) < len(self.files)):
			output = TAG_LOCATION + self.tags[self.cursor_swap[0]] + "/" + self.files[self.cursor[0] - len(self.directories)]
			output = os.path.dirname(os.path.realpath(output))
		with open(OUTPUTFILE, "w+") as f:
			f.write(output)
		self.kill_switch = True

	def append_tag (self):
		self.mode = self.modes.append

		self.update_context_bar("Please enter name of tag: ")
		tagname = self.context_bar.getstr().decode("utf-8")

		self.update_context_bar("Validating tagname")
		if (tagname in self.tags):
			self.update_context_bar("Tag already exists")
		elif (" " in tagname):
			self.update_context_bar("Tag cannot (yet) contain spaces")
		else:
			os.mkdir(TAG_LOCATION+tagname)
			self.init_tags()
			self.update_context_bar(f"Created new Tag: {tagname}")

		self.mode = self.modes.navigate

	def delete_action (self):
		self.mode = self.modes.delete
		if (self.cursor[1] == 0):
			selected = self.tags[self.cursor[0]]
			self.update_context_bar(f"Are you sure you want to delete the tag {selected}? (y/n) : ")
			response = self.context_bar.getstr().decode("utf-8")
			if (not response in ["y","Y","Yes","yes"]):
				self.update_context_bar("Tag was not deleted.")
			else:
				selected_path = TAG_LOCATION + selected
				if (len(self.directories)):
					[os.remove(selected_path+"/"+x) for x in self.directories]
				if (len(self.files)):
					[os.remove(selected_path+"/"+x) for x in self.files]
				os.rmdir(selected_path)
				self.init_tags()
				self.load_contents(self.tags[self.cursor[0]])
				self.draw_windows()
				self.update_context_bar(f"Removed Tag {selected}")
		else:
			selected = self.directories[self.cursor[0]] if self.cursor[0] < len(self.directories) else self.files[self.cursor[0] - len(self.directories)]
			self.update_context_bar(f"Are you sure you want to untag {selected}? (y/n) : ")
			response = self.context_bar.getstr().decode("utf-8")
			if (response in ["y","Y","Yes","yes"]):
				selected_path = TAG_LOCATION + self.tags[self.cursor_swap[0]] + "/" + selected
				os.remove(selected_path)
				self.load_contents(self.tags[self.cursor_swap[0]])
				if (len(self.files) + len(self.directories) == 0):
					self.cursor = self.cursor_swap
				self.draw_windows()
				self.update_context_bar(f"{self.tags[self.cursor_swap[0]]} tag was removed from {selected}.")
			else:
				self.update_context_bar(f"Tag was not removed from {selected}.")
		self.mode = self.modes.navigate
		self.handle_key()

	def handle_key (self):
		global OUTPUTFILE
		self.left_win.refresh()
		self.right_win.refresh()
		self.context_bar.refresh()
		key_event = self.stdscr.getch()
		events = {
			curses.KEY_UP : self.navigation,
			curses.KEY_DOWN : self.navigation,
			curses.KEY_LEFT : self.navigation,
			curses.KEY_RIGHT : self.navigation,
			curses.KEY_ENTER : lambda x: self.enter_action(),
			10 : lambda x: self.enter_action(),
			ord("q") : lambda x: setattr(self, "kill_switch", True),
			ord("n") : lambda x: self.append_tag(),
			curses.KEY_DC : lambda x: self.delete_action()
		}
		if (key_event in events.keys()):
			events[key_event](key_event)

	def mainloop (self):
		self.draw_windows()
		while not self.kill_switch:
			self.draw_windows()
			self.handle_key()


def main (thingy):
	with open(OUTPUTFILE, "w+") as f:
		f.write("")
	window = twoColumn(thingy)
	window.mainloop()
	curses.endwin()

if __name__ == "__main__":
	try:
		main(curses.initscr())
	except KeyboardInterrupt as e:
		try:
			curses.endwin()
		except Exception:
			pass
		exit()