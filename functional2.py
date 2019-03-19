from interpreter.clean import clean
from interpreter.interpret import interpret
import sys

if __name__ == '__main__':
	lines = []
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()
	lines = clean(lines)
	interpret(lines)