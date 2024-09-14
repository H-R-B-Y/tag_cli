#!/usr/bin/python3
import subprocess


def test():
	pipe = subprocess.Popen(["git", "status"], stdout=subprocess.PIPE)
	print(pipe.communicate()[0].decode("utf-8"))

if __name__ == "__main__":	
	test()