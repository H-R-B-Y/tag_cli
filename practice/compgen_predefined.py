import os

static_keywords = [
	"",
	""
]

temp, directories, temp2 = next(os.walk(os.path.expanduser(os.environ["TAGS_DIR"])))
dynamic_keywords = directories

[print(x) if " " not in x else print("\"" + x + "\"") for x in static_keywords]
[print(x) if " " not in x else print("\"" + x + "\"") for x in dynamic_keywords]