from random import randint

sik1 = open(r"C:\Users\sande\Desktop\Deepu\CodeChallenges\beale.wordlist.txt", 'r').read().split()[4:]
sik = sik1.copy()
def pw(n):
	for i in range(n):
		roll = ''
		for i in range(5):
			roll += str(randint(1,6))
		print(sik[sik.index(roll)+1], end = ' ')
pw(5)