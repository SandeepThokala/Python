from random import choice
from itertools import combinations, product


def dice(*args):
	l = []
	for i in range(len(args)):
		l.append([*(range(1,args[i]+1))])
	sums = {sum(i) for i in product(*(j for j in l))}
	outcomes = []
	for i in range(100**3):
		outcomes.append(sum(tuple(choice(range(1, 1+i)) for i in args)))
	for i in sums:
		print(f'{i}: {outcomes.count(i)/1000000}')

dice(4,6,6)