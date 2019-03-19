from interpreter.tests import isnum

class Environment:
	def __init__(self):
		self.variables = {}
		self.__prefix__ = ""
		
	def __str__(self):
		return str(self.variables)
	
	def prefix(self, prefix):
		self.__prefix__ = prefix
		
	def merge(self, env):
		newdict = {}
		for key, value in env.variables.items():
			key = env.__prefix__ + str(key)
			newdict[key] = value
		self.variables.update(newdict)
	
	def push(self, val):
		count = 0
		for key, _ in self.variables.items():
			if isnum(key):
				count += 1
		self.variables[count] = val
		return val
	
	def pop(self, key):
		return self.variables.pop(key, None)