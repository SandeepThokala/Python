#my solution

def ss(x):
	l = x.split()
	l.sort(key = lambda x: x[0].lower())
	return ' '.join(l)

print(ss('Hi andi Uppal baalu andi'))

