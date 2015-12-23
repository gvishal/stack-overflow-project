import ast
def get_pattern():
	fp = open("sorted.txt","r")
	index = 0
	x = fp.readline()
	flag = 0
	count = 0
	patterns = []
	while(len(x)>2):
		print index
		index = index + 1
		if(index == 46):
			flag = 1
		if(flag == 1):
			pattern = ast.literal_eval(x.split("\n")[0])[0]
			pattern = pattern.split(" ")
			print pattern
			count = count + 1
			patterns.append(pattern)
			if(count == 20):
				return patterns
		x = fp.readline()

