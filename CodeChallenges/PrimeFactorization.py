#my solution

def prime(x):
	count = 0
	for i in range(1, int(x/2) + 1):
		if not(x%i):
			count += 1
			if count > 1:
				break
	return 1 if count == 1 else 0


def func(x):
	p, l = [], []
	for i in range(1, int(x/2) + 1):
		if not(x%i) and prime(i):
			p.append(i) 
	for i in p:
		while not(x%i):
			l.append(i)
			x /= i
	return f'Prime factorisation: {[x] if prime(x) else l}'

#print(func(int(input('Enter: '))))

#not my solution :(

def get_prime_factors(n):
	factors = []
	d = 2
	while(d <= n):
		if (n % d) == 0:
			factors.append(d)
			n = n/d
		else:
			d += 1
	return factors

print(get_prime_factors(26908006))

#x = int(input('Enter: '))

#print(*(prime(i) for i in range(1, 1001)), sep = '\n' if prime(i) == 1 else ' ,')