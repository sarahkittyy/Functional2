import re

def isnum(val):
	try:
		y = float(val)
	except ValueError:
		return False
	except TypeError:
		return False
	return True
	
def isquoted(val):
	if not isinstance(val, str):
		return False
	else:
		return (re.match(r'^("|\').*("|\')$', val) != None)
		
def islambda(val):
	return (re.match(r'\{.*\}', val) != None)

def iscall(val):
	return (re.match(r'^\w*\.(.*)$', val) != None)