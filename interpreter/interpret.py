###

from interpreter.tests import isnum, isquoted, islambda, iscall
from interpreter.strip import evalexpr, docall
from interpreter.env import Environment
import re

env = Environment()

def interpret(lines):
	
	env.variables["out"] = lambda x : print(x, end='')
	env.variables["in"] = lambda x : input(x)
	
	for line in lines:
		interpret_line(line)
		
def interpret_line(line):
	# assignment
	x = re.match(r'(.*)=(.*)', line)
	if x != None:
		name = x.group(1)
		value = x.group(2)
		if isnum(value):
			value = float(value)
		elif isquoted(value):
			value = value.strip()[1:-1]
		elif islambda(value):
			value = evalexpr(value[1:-1], env)
		env.variables[name] = value
	# calls
	elif iscall(line):
		docall(line, env)