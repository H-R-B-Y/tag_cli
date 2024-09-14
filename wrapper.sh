#!/bin/bash

# This needs to be documented better please!!!!!!!

export TAGS_DIR=""
export SCRIPT_DIR=""

function tagger() {
	# Path to the tags directory
	
	PATH_TO_UI="$SCRIPT_DIR/user_interface.py"
	PATH_TO_REDIRECT="$SCRIPT_DIR/navto"

	# Check if no arguments are provided
	if [ $# -eq 0 ]; then
		python3 $PATH_TO_UI 3>&1 1>&2 2>&3
		directory=$(realpath $(cat $PATH_TO_REDIRECT) 2>/dev/null)
		if [ -d $directory ] && [ "$directory" != "" ]; then
			cd $directory
			if [ $? -ne 0 ]; then
				echo "Error: Failed to navigate to $directory"
				exit 1
			else
				echo "" > $PATH_TO_REDIRECT
			fi
			
		fi
	fi

	if [ $# -eq 1 ]; then
		command="$1"
		case $command in 
			"list")
				ls $TAGS_DIR
				;;
			"--update")
				python3 $PATH_TO_UI --update 
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
			return 1
		fi
		if [ ! -d "$TAGS_DIR/$tag_name" ]; then
			echo "The tag '$tag_name' must be an existing file in the '~/Tags' directory."
			return 1
		fi
		if [ ! -e "$destination" ] || [ "$destination " == ""]; then
			echo "The destination directory '$destination_dir' does not exist."
			read -p "Would you like to create the destination directory? (y/n): " choice
			if [ "$choice" == "y" ]; then
				mkdir -p "$destination"
				if [ $? -eq 0 ]; then
					echo "Destination directory created: $destination"
				else
					echo "Error: Failed to create destination directory."
					return 1
				fi
			else
				echo "Exiting..."
				return 1
			fi
		fi

		ln -s "$(realpath "$destination")" "$TAGS_DIR/$tag_name/$(basename "$destination")"
		if [ $? -eq 0 ]; then
			echo "Symlink created: $TAGS_DIR/$tag_name/$(basename "$destination") -> $destination"
		else
			echo "Error: Failed to create symlink."
			return 1
		fi
	fi
}

_local_files()
{
	local dir="$(pwd)"

	pushd "$dir" >/dev/null
	find * -maxdepth 0 2>/dev/null
	popd >/dev/null
}

_tagger_completions() {
	local cur prev opts
	cur="${COMP_WORDS[COMP_CWORD]}"
	prev="${COMP_WORDS[COMP_CWORD-1]}"
	TAGS_DIR="$HOME/Tags"
	local IFS=$'\n'

	if [ $COMP_CWORD -eq 1 ]; then
		opts=$(find "$TAGS_DIR"/* -maxdepth 0 -printf "%f\n" 2>/dev/null)
		opts="${opts}$'\n'list"
		COMPREPLY=( $(compgen -W "$opts" -- "$cur"))
	elif [ $COMP_CWORD -eq 2 ]; then
		if [ -d "$TAGS_DIR/${prev//\\/}" ]; then
			COMPREPLY=( $(compgen -W "$(_local_files)" -- "$cur") )
		fi
	fi
}

complete -F _tagger_completions tagger
