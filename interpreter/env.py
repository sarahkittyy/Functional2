class Environment:
	def __init__(self):
		self.variables = {}
		self.__prefix__ = ""
		
	def __str__(self):
		return str(self.variables)
	
	def prefix(self, prefix):
		# strip the old prefix
		newvars = {}
		for variable, value in self.variables.items():
			variable = variable[len(self.__prefix__):]
			newvars[variable] = value
		self.variables = newvars
		# set the new prefix
		self.__prefix__ = prefix
		newvars = {}
		for variable, value in self.variables.items():
			variable = self.__prefix__ + variable
			newvars[variable] = value
		self.variables = newvars
		
	def merge(self, env):
		self.variables.update(env.variables)