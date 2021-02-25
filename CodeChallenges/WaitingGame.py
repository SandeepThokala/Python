from time import time, sleep
from random import randint

def game():
	if input('\n------ PRESS ENTER ------') == '':
		t = randint(2,6)
		sleep(1)
		print(f'------ PRESS ENTER, AGAIN, IN {t} SECONDS ------\nStarting from....')
		sleep(1)
		for i in [3,2,1]:
			print(f'{i}....')
			sleep(1)
		print('NOW...')
		t1 = time()
		sleep(t)
		input()
		t2 = time()
		if round(t2 - t1) == t:
			print(f'Right on....\nYou pressed exactly after {t} seconds and {round((t2 - t - t1)*1000)} milli seconds!!!!')
		else:
			print(f'Booo...\nYou were late by {round((t2 - t1 - t))} seconds')
	else:
		game()

game()

