#my solution

import re
def isp(x):
	x = re.sub(r'[^\w\s]','', x)
	return True if x[::-1].lower() == x.lower() else False

print(isp('race-caR'))

#not my solution :(

def is_palindrome(phrase):
	forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
	backwards = forwards[::-1]
	return forwards == backwards

print(is_palindrome("go hang a salami - I'm a lasagna hog"))

