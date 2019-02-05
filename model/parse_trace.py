from pandas import read_table, DataFrame, date_range, concat
from sys import exit
import os
import sys
import re

def parse(fname):
	f = open(fname, 'r', encoding='utf16')

	lines = []
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
	vars, states = [], []
	for l in lines:
		a = l.split(')')
		vars.append(a[1].split(" "))
		states.append(a[0].replace('( ','').strip().split(" "))


	name	= lambda sep,x: x.split(sep)[0]
	value	= lambda sep,x: x.split(sep)[1]

	vars_ = DataFrame(
		data = vars,
		columns = [name('=',x) for x in vars[0]],
	).applymap(lambda x:int(value('=', x)))

	states_ = DataFrame(
		data = states,
		columns = [name('.',x) for x in states[0]],
	).applymap(lambda x:value('.', x))

	return concat([vars_, states_], axis=1)

if __name__== "__main__":
	df = parse(str(sys.argv[1]))
	df.to_csv("out.csv")
	df[['time', 'B.load']].drop_duplicates(keep='first').to_csv("kibam.csv",header=False, index=False)
