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
			key = env.__prefix__ + key
			newdict[key] = value
		self.variables.update(newdict)