# Tag UI and wrapper function.

Tag UI used for navigating to tagged files/folders.

Wrapper function to be sourced in shell rc file so that cd is run in the current shell instance.


## To Do:
- Sub-Tagging? (thinking either AND groupings or sub directories?) (V2)
- Would be nice to implement the preview window ?_? (V2)
- __Setup script! (previously marked as done! I was wrong T-T)__
- ~~Make the code cleaner T-T~~
- ~~Ability to resize the window without it breaking :D~~
- ~~Allow lists longer than the row count!!!!!~~
- ~~Ability to add tags through the UI.~~
- ~~Ability to untag items through the UI.~~
- ~~Remove hard coded links~~ (It is still hard coded but using a single source!)
- ~~Update delete code to avoid situation where the line is too long to read new characters!~~ (Not perfect but works for now)
- ~~Cleanup dynamic calculations in favour of static single sources!~~
- ~~Make selection cleaner~~ (Moved to class property)
- ~~Figure out how to allow spaces in tag names in conjunction with the tab completion (a space in a tags name gets split into multiple completion targets T-T)~~ (Tags with spaces in are __working?__)


## Setup:
- Run the install.sh script
- reload your shell config (i.e. `source ~/.bashrc`)

## Usage:
- `tagger` can be run from the terminal to run the UI.
	- from the UI `n` can be used to create a new tag.
- `tagger {name of tag} {path to a file}` will tag the specified file
- New tags can be manually created using `mkdir {tagname}` in the tag directory specified during installation.


## Uninstall
- To uninstall remove the line:
`source {path to your installation}/wrapper.sh`
from the shell rc file specified during installation.
