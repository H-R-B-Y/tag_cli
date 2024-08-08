#!/bin/bash

# This needs to be documented better please!!!!!!!

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

	if [ $# -eq 1 ]; then
		command="$1"
		case $command in 
			"list")
				ls $TAGS_DIR
				;;
			*)
				echo "need to print usage here!"
				;;
		esac
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

_tagger_completions() {
	local cur prev opts
	cur="${COMP_WORDS[COMP_CWORD]}"
	prev="${COMP_WORDS[COMP_CWORD-1]}"
	TAGS_DIR="$HOME/Tags"

	if [ $COMP_CWORD -eq 1 ]; then
		opts=$(ls --quoting-style=escape $TAGS_DIR)
		opts="${opts} list"
		COMPREPLY=( $(compgen -W "$opts" -- "$cur") )
	elif [ $COMP_CWORD -eq 2 ]; then
		if [ -d "$TAGS_DIR/$prev" ]; then
			COMPREPLY=( $(compgen -W "$(ls .)" -- "$cur") )
		fi
	fi
}

complete -F _tagger_completions tagger