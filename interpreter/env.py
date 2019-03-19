class Environment:
	def __init__(self):
		self.variables = {}
		
	def __str__(self):
		return str(self.variables)
		
	def merge(self, env):
		self.variables.update(env.variables)