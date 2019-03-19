from interpreter.clean import clean
from interpreter.interpret import interpret
import sys
import os
import re

def runFile(filename):
	lines = []
	path = ""
	with open(filename, 'r+') as f:
		line = f.read()
		pat = re.compile('(.*)~\\$.*', re.MULTILINE)
		line = re.sub(pat, '\\1', line)
		lines = line.split(';')
	lines = clean(lines)
	return interpret(lines, path + '/')

if __name__ == '__main__':
	runFile(sys.argv[1])