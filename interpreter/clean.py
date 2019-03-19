import re

def removeSpaces(line):
	depth = False
	ret = ""
	for char in line:
		if char in ['"', "'"]:
			depth = not depth
		if depth:
			ret += char
		elif not depth and re.match('\\s', char) == None:
			ret += char
	return ret

def clean(lines):
	cleaned = []
	for line in lines:
		line = removeSpaces(line)
		line = re.sub(r'^\s*$', '', line)
		line = re.sub(r'(.*)~\$.*', '\\1', line)
		if line:
			cleaned.append(line)
	return cleaned