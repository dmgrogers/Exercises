
# DRY vs WET code (don't repeat yourself vs write everything twice)
# Abstracting (ie reusing code others have written without reinventing)

###############################

# def
def hello():
	print('hello world')

hello()

###############################

# return:
# return exits the function, and the function outputs whatever comes after the return keyword
# multiple outputs require a tuple after the return

# A coin flip function
# random:
from random import randint
from random import random
a = [randint(0,2) for i in range(20)]
a

b = [random() for i in range(20)]
b

# Define a function that yields heads or tails randomly when called
# one way
def flip():
	if randint(0,1)==0:
		return 'heads'
	else:
		return 'tails'

# Another way:
def flip2():
	if random()>0.5:
		return 'heads'
	else:
		return 'tails'


flip()
flip2()


# Functions with parameters (which take arguments)
def cube(x):       # x is the parameter
	if type(x) is str:
		return x+x+x
	else:
		return x**3


cube(0.5)          # 0.5 is the argument
cube('a') 


###############################

# Common mistakes: improper indentation, and superfluous code
# improper indentation:
def sum_numbers_wrong(list):
	total = 0
	for n in list:
		total += n 
		return total


def sum_numbers_right(list):
	total = 0
	for n in list:
		total += n 
	return total


sum_numbers_wrong([1,2,3,4]) # return exits the function too soon
sum_numbers_right([1,2,3,4])


# Superfluous code:
def is_odd(n):
	if n%2==0:
		return True
	return False       # an 'else' is not necessary here

is_odd(10)
is_odd(11)



# Default parameters (can be especially useful for testing)
# Parameters with defaults need to follow non-default parameters
def power(x='Power',p=2):       # x is the parameter
	if type(x) is str:
		return x*p
	else:
		return x**p


power() # no parameters need to be given to check basic functionality
power(12,3)

def monsters(monster='dragon'):
	monsters = {'hydra':'regrow heads','dragon':'breathe fire'}
	return f'{monster}s do this: {monsters.get(monster)}'

monsters()

###############################

# Keyword arguments:
# So that arguments can be assigned to parameters independently of order

def power(x='Power',p=2):       # x is the parameter
	if type(x) is str:
		return x*p
	else:
		return x**p


power(3,'Aa')  # error
power(p=3,x='Aa')  # no error, using keyword argument


###############################

# Scope: where variables are available

# variables created within a function are only accessible within it

def return_one():
	z=1
	return z


return_one()
z                # error: z is scoped only in the function


y='global'   # this variable is a global variable, defined independent of a function
def addA():
	y+='A'
	return y


addA() # local variable 'y' referenced before assignment

# Best to avoid global variables.
# However, if needed:
y='global'   # this variable is a global variable, defined independent of a function
def addAAA():
	global y  # first, tell python to look for a global rather than a local variable
	y+='AAA'
	return y


addAAA()


# This restriction on using global variables only applies to altering them
# We can access them, though:
y='global' 
def printY():
	print(y)

printY()


# nonlocal keyword: for altering parent's local variables within child functions

def parent():
	i=0
	def child():
		i+=1
		return i
	return child()


parent()       # local variable i referenced before assignment


def parent1():
	i=0
	def child():
		nonlocal i   # allows the child function to treat the nonlocal variable i as local (and therefore alterable)
		i+=1
		return i
	return child()


parent1()  # returns 1 as expected



# Docstrings: for documenting functions: """ and [function].__doc__

def dox():
	"""This illustrates the use of docstrings"""
	print("this function is well-documented; use the .__doc__ attribute")


dox()
dox.__doc__



