
h='Hello world'
def doubleLetters(s='Hello world'):
	ll=list(map(lambda x:x*2,s)) # maps the string onto a new iterable with the function x*2 doubling each element
	ss=''.join(ll)
	return ss

doubleLetters()
doubleLetters('Goodnight')
