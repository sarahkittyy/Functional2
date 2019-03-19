from interpreter.clean import clean
from interpreter.interpret import interpret
import sys
import os

def runFile(filename):
	lines = []
	path = ""
	with open(filename, 'r+') as f:
		lines = f.readlines()
		path = os.path.dirname(f.name)
	lines = clean(lines)
	return interpret(lines, path + '/')

if __name__ == '__main__':
	runFile(sys.argv[1])