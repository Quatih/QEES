from pandas import read_table, DataFrame, date_range, concat
from sys import exit
import os
import sys
import re

def parse(fname):
	if isinstance(fname, str):
		f = open(fname, 'r')
	else:
		exit('fname must either be a path to a file')

	lines = []
	print("start")
	content = f.read().splitlines()
	for i in range(len(content)):
		if "State:" in content[i]:
			arr = []
			for j in range(i+1, len(content)):
				if "Trans" in content[j]:
					lines.append(''.join(arr))
					i = j
					break
				elif "Del" in content[j]:
					lines.append(''.join(arr))
					i = j
					break
				else:
					arr.append(content[j])
	print(lines)
	var_lst, state_lst = [], []
	for l in lines:

		a = l.split(')')
		var_lst.append(a[1].split(" "))
		state_lst.append(a[0].replace('( ','').strip().split(" "))

	print(state_lst)
	# b = f.read()
	# b = b.replace('\n', '')

	# for block in b.split(''):
		
	# 	if "State:" in block:
	# 		a = block
	# 		a = a.replace('\n', '')
	# 		parts = a.split(')')
	# 		print(parts)
	# 		var_lst.append(parts[-1])
	# 		b = parts[0].strip().split('( ')
	# 		state_lst.append(b[-1])
			
	# 	## PARSING TRANSITIONS MIGHT NOT BE NECESSARY
	# f.close()


	# a = [x.split(" ") for x in var_lst]
	# #b = [c[0].split("=")[1] for c in a]
	# print(b)
	name	= lambda sep,x: x.split(sep)[0]
	value	= lambda sep,x: x.split(sep)[1]

	vars = DataFrame(
		data = var_lst,
		columns = [name('=',x) for x in var_lst[0]],
	).applymap(lambda x:int(value('=', x)))

	states = DataFrame(
		data = state_lst,
		columns = [name('.',x) for x in state_lst[0]],
	).applymap(lambda x:value('.', x))

	return concat([vars, states], axis=1)

df = parse("trace.txt")
df.to_csv("out.csv")
