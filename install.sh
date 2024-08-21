
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
		echo "Creatign $tag_directory..."
		mkdir -p "${tag_directory}"
	else
		echo "Installation aborted."
		exit 1
	fi

elif [ ! -d "$tag_directory" ]; then
	echo "Specified path is not a directory."
	echo "Installation aborted."
	exit 1

elif [ -d "$tag_directory" ]; then
	echo "Tag directory exists."
fi

echo "Using current path as install directory."

if [ ! -e "./wrapper.sh" ]; then
	echo "Wrapper script not found, Aborting."
	exit 1
fi

ins_text="export TAGS_DIR=\"$tag_directory\""
scr_text="export SCRIPT_DIR=\"$(pwd)\""

sed -i "5s|.*|$ins_text|" ./wrapper.sh
sed -i "6s|.*|$scr_text|" ./wrapper.sh

echo "Wrapper file has been updated."

echo "Wrapper file needs to be sourced in your shell rc file."
read -p "Please enter the location of the rc file [default: ~/.bashrc]: " rc_location
rc_location=${rc_location:-~/.bashrc}  # Use default if no input
rc_location="${rc_location/#\~/$HOME}"
echo "Sourcing wrapper in $rc_location..."
echo "source $(pwd)/wrapper.sh" >> $rc_location
echo "Done!"
echo "Installation complete!"