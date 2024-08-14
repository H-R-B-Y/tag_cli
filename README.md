# Tag UI and wrapper function.

Tag UI used for navigating to tagged files/folders.

Wrapper function to be sourced in shell rc file so that cd is run in the current shell instance.


## To Do:
- Setup script! (V2)
- Sub-Tagging? (thinking either AND groupings or sub directories?) (V2)
- Would be nice to implement the preview window ?_? (V2)
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
- Create Tags folder in `$HOME`
- Source wrapper.sh in `.{insert shell name here}rc`
- Update the `$SCRIPT_DIR` in wrapper.sh to reflect where tag_cli is installed!