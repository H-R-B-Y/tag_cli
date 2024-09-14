# Tag UI and wrapper function.

Tag UI used for navigating to tagged files/folders.

Wrapper function to be sourced in shell rc file so that cd is run in the current shell instance.


## To Do:
- Sub-Tagging? (thinking either AND groupings or sub directories?) (V2)
- Would be nice to implement the preview window ?_? (V2)
- __Setup script! (Still a work in progress):__
	1. Doesnt work on mac
	2. Doesnt work without sed
	3. i have no idea how to init bashcompinit on other shells
- ~~Figure out how to allow spaces in tag names in conjunction with the tab completion (a space in a tags name gets split into multiple completion targets T-T)~~ (Tags with spaces in are __working?__)


## Setup:
- Run the install.sh script
- reload your shell config (i.e. `source ~/.bashrc`)

## Usage:
- `tagger` can be run from the terminal to run the UI.
	- from the UI `n` can be used to create a new tag.
- `tagger {name of tag} {path to a file}` will tag the specified file
- New tags can be manually created using `mkdir {tagname}` in the tag directory specified during installation.
- `tagger --update` will check for updates and safely update the main scripts without overwriting your changes.


## Uninstall
- To uninstall remove the line:
`source {path to your installation}/wrapper.sh`
from the shell rc file specified during installation.
