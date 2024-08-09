# Tag UI and wrapper function.

Tag UI used for navigating to tagged files/folders.

Wrapper function to be sourced in shell rc file so that cd is run in the current shell instance.


## To Do:
- ~~Allow lists longer than the row count!!!!!~~
- ~~Ability to add tags through the UI.~~
- ~~Ability to untag items through the UI.~~
- ~~Remove hard coded links~~ (It is still hard coded but using a single source!)
- Update delete code to avoid situation where the line is too long to read new characters!
- Figure out how to allow spaces in tag names in conjunction with the tab completion (a space in a tags name gets split into multiple completion targets T-T)
- Would be nice to implement the preview window ?_?
- Cleanup dynamic calculations in favour of static single sources!
- Make selection cleaner (stop dynamically calculating the offset + position to figure out what is currently selected, return value of funtion get_selected) 

## Setup:
- Create Tags folder in `$HOME`
- Source wrapper.sh in `.{insert shell name here}rc`
- Update the `$SCRIPT_DIR` in wrapper.sh to reflect where tag_cli is installed!