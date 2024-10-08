#!/bin/bash

ask_yes_no() {
	while true; do
		read -p "$1 [y/n]: " yn
		case $yn in
			[Yy]* ) return 0;;  # Return 0 for 'yes'
			[Nn]* ) return 1;;  # Return 1 for 'no'
			* ) echo "Please answer yes or no.";;
		esac
	done
}

echo ""
echo "Tag folder setup."

read -p "Enter the tag directory [default: ~/Tags]: " tag_directory
tag_directory=${tag_directory:-~/Tags}  # Use default if no input
tag_directory="${tag_directory/#\~/$HOME}"

if [ ! -e "$tag_directory" ]; then
	# Confirm the Tag directory
	if ask_yes_no "Create $tag_directory?"; then
		echo "Creating $tag_directory..."
		mkdir -p "${tag_directory}"
		mkdir -p "${tag_directory}/default"
	else
		echo "Installation aborted."
		exit 1
	fi
elif [ ! -d "$tag_directory" ]; then
	echo "Specified path is not a directory."
	echo "Installation aborted."
	exit 1
else
	echo "Tag directory exists."
	if [ -z "$( ls -A '/path/to/dir' )" ]; then
		mkdir -p "${tag_directory}/default"
	fi
fi

echo "Using current path as install directory."

if [ ! -e "./wrapper.sh" ]; then
	echo "Wrapper script not found. Aborting."
	exit 1
fi

ins_text="export TAGS_DIR=\"$tag_directory\""
scr_text="export SCRIPT_DIR=\"$(pwd)\""

if [[ "$OSTYPE" != "darwin"* ]]; then
	if ! command -v sed >/dev/null 2>&1; then
		echo "sed is not installed. Please install sed and try again."
		exit 1
	fi
	sed -i "5s|.*|$ins_text|" ./wrapper.sh
	sed -i "6s|.*|$scr_text|" ./wrapper.sh
else
	echo "Making this work on MacOS is left as an exercise for the reader. (I am lazy)"
	echo "Please update the following lines in wrapper.sh:"
	echo "export TAGS_DIR=\"\$HOME/Tags\""
	echo "export SCRIPT_DIR=\"$(pwd)\""
fi

echo "Wrapper file has been updated."

read -p "Please enter the location of the rc file [default: ~/.bashrc]: " rc_location
rc_location=${rc_location:-~/.bashrc}  # Use default if no input
rc_location="${rc_location/#\~/$HOME}"

echo "Sourcing wrapper in $rc_location..."
if [[ "$rc_location" == *".zshrc" ]]; then
	echo "Detected zsh configuration file."
	if ! grep -q "autoload -U bashcompinit && bashcompinit" "$rc_location"; then
		echo "Adding bashcompinit to $rc_location..."
		echo "autoload -U bashcompinit && bashcompinit" >> "$rc_location"
	fi
fi

echo "source $(pwd)/wrapper.sh" >> "$rc_location"
echo "Done!"
echo "Installation complete!"
