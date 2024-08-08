# Tag UI and wrapper function.

Tag UI used for navigating to tagged files/folders.

Wrapper function to be sourced in shell rc file so that cd is run in the current shell instance.


## To Do:
- Allow lists longer than the row count!!!!!
- ~~Ability to add tags through the UI.~~
- ~~Ability to untag items through the UI.~~
- Remove hard coded links
- Figure out how to allow spaces in tag names in conjunction with the tab completion (a space in a tags name gets split into multiple completion targets T-T)

## Setup:
- Create Tags folder in `$HOME`
- Source wrapper.sh in `.{insert shell name here}rc`
- Update hard coded links if needed 