#!/bin/bash
function tagger() {
	# Path to the tags directory
	TAGS_DIR="$HOME/Tags"

	SCRIPT_DIR=/home/harvey/Documents/tag_cli/
	PATH_TO_UI="$SCRIPT_DIR/user_interface.py"
	PATH_TO_REDIRECT="$SCRIPT_DIR/navto"


	# Check if no arguments are provided
	if [ $# -eq 0 ]; then
		python3 $PATH_TO_UI 3>&1 1>&2 2>&3
		directory=$(cat $PATH_TO_REDIRECT)
		cd "$directory"
	fi

	if [ $# -eq 2 ]; then
		tag_name="$1"
		destination="$2"

		if [ -z "$tag_name" ]; then
			echo "First argument must be a non-empty string."
			usage
		fi
		if [ ! -d "$TAGS_DIR/$tag_name" ]; then
			echo "The tag '$tag_name' must be an existing file in the '~/Tags' directory."
			usage
		fi
		if [ ! -e "$destination" ]; then
			echo "The destination directory '$destination_dir' does not exist."
			usage
		fi

		ln -s "$(realpath $destination)" "$TAGS_DIR/$tag_name/$(basename "$destination")"
		echo "Symlink created: $TAGS_DIR/$tag_name/$(basename "$destination") -> $destination"
	fi
}