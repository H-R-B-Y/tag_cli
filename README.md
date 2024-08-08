I don't like having to navigate around a filesystem to find where things are, MacOs tags inspired me to create a similar type of file structure.

On a high level I just created a Tags directory in $HOME, populated with folders to represent the tags, then whenever i would like to tag somehting i can just symlink the file/folder into the respective tag. 

The user interface can be used to view the tags and navigate to the directory of any tagged file/folder.

To Do:
- Sllow lists longer than the row count!!!!!
- Ability to add tags through the UI.
- Ability to untag items through the UI.
- Remove hard coded links
- Figure out how to allow spaces in tag names in conjunction with the tab completion (a space in a tags name gets split into multiple completion targets T-T)

Setup:
- Create Tags folder in `$HOME`
- Source wrapper.sh in .{insert shell name here}rc
- Update hard coded links if needed 