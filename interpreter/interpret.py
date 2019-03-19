###

from interpreter.tests import isnum, isquoted, islambda, iscall
from interpreter.strip import evalexpr, docall, isfullexpr
from interpreter.env import Environment
from interpreter.clean import clean
import re
import os

env = Environment()

def interpret(lines, path):
	def impfile(file):
		lines = []
		npath = ""
		with open(path + file, 'r+') as f:
			lines = f.readlines()
			npath = os.path.dirname(f.name)
		lines = clean(lines)
		env.merge(interpret(lines, npath + '/'))
	
	env.variables["out"] = lambda x : print(x, end='')
	env.variables["in"] = lambda x : input(x)
	env.variables["import"] = lambda x : impfile(x)
	
	for line in lines:
		interpret_line(line)
	return env
		
def interpret_line(line):
	# assignment
	x = re.match(r'(.*)=(.*)', line)
	if x != None:
		name = x.group(1)
		value = x.group(2)
		if isnum(value):
			value = float(value)
		elif iscall(value):
			value = docall(value, env)
		elif isquoted(value):
			value = value.strip()[1:-1]
		elif isfullexpr(value):
			value = evalexpr(value[1:-1], env)
		env.variables[name] = value
	# calls
	elif iscall(line):
		docall(line, env)