###

from interpreter.tests import isnum, isquoted, islambda, iscall
from interpreter.strip import evalexpr, docall, isfullexpr, isstack, getstack, interpret_line
from interpreter.env import Environment
from interpreter.clean import clean
import re
import os

def interpret(lines, path):
	env = Environment()
	
	def impfile(file):
		lines = []
		npath = ""
		with open(path + file, 'r+') as f:
			line = f.read()
			pat = re.compile('(.*)~\\$.*', re.MULTILINE)
			line = re.sub(pat, '\\1', line)
			lines = line.split(';')
			npath = os.path.dirname(f.name)
		lines = clean(lines)
		newenv = interpret(lines, npath + '/')
		env.merge(newenv)
		
	env.variables["out"] = lambda x : print(x, end='')
	env.variables["in"] = lambda x : input(x)
	env.variables["import"] = lambda x : impfile(x)
	env.variables["package"] = lambda x : env.prefix(x)
	env.variables["get"] = lambda x : (lambda y : x.variables.get(y, None))
	
	for line in lines:
		interpret_line(line, env)
	return env