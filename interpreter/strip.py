from interpreter.env import Environment
from interpreter.tests import isnum, iscall, isquoted
from interpreter.error import error
import re
import copy
from interpreter.clean import removeSpaces

# takes in a string, and returns the inner code tree.
def evalexpr(value, env: Environment):
	if isnum(value):
		return float(value)
	elif isfullexpr(value):
		return evalexpr(value[1:-1], env)
	elif islambda(value):
		return getlambda(value, env)
	elif isquoted(value):
		str = removeSpaces(value)[1:-1]
		str = re.sub(r'\\n','\n',str)
		return str
	elif ismath(value):
		return domath(value, env)
	elif iscall(value):
		return docall(value, env)
	elif isternary(value):
		return doternary(value, env)
	elif isvar(value, env) != None:
		return env.variables[value]
	else:
		error('Expression "' + value +'" unable to be evaluated.')
		
def isternary(value):
	return (re.match(r'.*\?.*\:.*', value) != None)

def doternary(value, env: Environment):
	def splitOuter(str, left, right, splits):
		outer = []
		cstr = ""
		depth = 0
		for char in str:
			was = False
			if char == left:
				depth += 1
			elif char == right:
				depth -= 1
			if depth == 0:
				if char in splits:
					outer.append(cstr)
					cstr = ""
					was = True
			if not was:
				cstr += char
		outer.append(cstr)
		if len(outer) != 3:
			error('Invalid ternary operator ' + str)
			return ['','','']
		return outer
		
	cond, true, false = splitOuter(value, '{', '}', '?:')[:3]
	return evalexpr(true, env) if evalexpr(cond, env) != 0 else evalexpr(false, env)
	

def docall(value, env: Environment):
	def get(value: str):
		cstr = ""
		first = None
		depth = 0
		for char in value:
			if first != None:
				cstr += char
				continue
			if char == '{':
				depth += 1
			elif char == '}':
				depth -= 1
			if depth == 0:
				if char == '.':
					first = cstr
					cstr = ""
					continue
			cstr += char
		return first,cstr
	
	before, after = get(value)
	before = evalexpr(before, env)
	after = evalexpr(after, env)
	if not callable(before):
		error(str(before) + ' not a callable object.')
	res = before(after)
	return res
		
		
def isfullexpr(value):
	depth = 0
	hit = False
	for char in value:
		if char == '{':
			depth += 1
			hit = True
		if hit and depth == 0:
			return False
		elif char == '}':
			depth -= 1
			hit = True
	return depth == 0 and hit and (re.match(r'^\{.*\}$', value) != None)
	# return (re.match(r'^\{[^(\}|\{)]*\}$', value) != None)

def isvar(value, env: Environment):
	return env.variables.get(value, None)
	
def islambda(value):
	return (re.match(r'(.*)->(.*)', value) != None)
	
def getlambda(value, env: Environment):
	def getname(value: str):
		cstr = ""
		for char in value:
			if char == '-':
				return cstr
			else:
				cstr += char
		return None
	def getparams(value: str):
		cstr = ""
		hit = False
		for char in value:
			if hit:
				cstr += char
			if char == '>':
				hit = True
		return cstr
		
	left = getname(value)
	right = getparams(value)
	
	def dolambdamath(l, r, v, env: Environment):
		tenv = copy.deepcopy(env)
		tenv.variables[l] = v
		return evalexpr(r, tenv)
	return lambda v : dolambdamath(left, right, v, env)
	
def ismath(value):
	depth = 0
	for char in value:
		if char == '{':
			depth += 1
		elif char == '}':
			depth -= 1
		
		if depth == 0 and char in '+-*/%&':
			return True
	return False
	
def domath(value, env: Environment):
	# get left, oper, right from the expression
	def splitOuter(str, left, right, splits):
		outer = []
		cstr = ""
		depth = 0
		for char in str:
			was = False
			if char == left:
				depth += 1
			elif char == right:
				depth -= 1
			if depth == 0:
				if char in splits:
					outer.append(cstr)
					outer.append(char)
					cstr = ""
					was = True
			if not was:
				cstr += char
		outer.append(cstr)
		if len(outer) != 3:
			error("Invalid mathematical operation " + str)
			return ['','','']
		return outer
	
	
	left, oper, right = splitOuter(value, '{', '}', '+-*/%&')[:3]

	left = evalexpr(left, env)
	right = evalexpr(right, env)
	if oper == '&':
		return left
	result = eval(str(left) + str(oper) + str(right))
	return result