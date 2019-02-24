# Tuples are ordered immutable iterables (similar to strings, but taking any data types as elements)
# They're faster than lists, and less prone to bugs via accidental modification
# Often used as locations, for example (latitude,longitude)
# They can be used as valid keys in a dictionary, unlike lists.
# Some dictionary items return tuples: .items() returns a list of 2-tuples


letters = 'abc'
l = ('a','b','c','c','b')
n = (1,2,3)
nl = [3,4,5]
nl_tuple=tuple(nl) # converting a list to a tuple
nl_tuple[0] # accessing tuple elements with indexes


# Iteration
for i in l:
	print(i)

i = len(l)-1
while i >= 0:
	print(str(i)+' '+l[i])
	i-=1

# slicing
l[0:]
l[::-1]

# Tuple methods (just 2):
# .count()
l.count('c') # counts occurrences

# .index()
l.index('b')  # returns index of first occurrence, error if absent



#############################
#############################
# Sets
# Non-ordered but iterable mutable collections of unique elements

s = {1,2,3,4,4}
s=set([1,2,3,4,4])  # equivalent
s # the extra 4 disappears

# 'in'
3 in s

# Iteration
for i in s:
	print(i)

# A common use case for sets: removing duplicates or counting unique values
list1 = [1,2,1,4,4,3,5,2,2,6,2,3,1,1]

set1=set(list1)
len(set(list1))
list(set(list1))

# Set methods: add, remove
set1.add('b')
set1

# remove (can throw an error)
set1.remove('c')
set1

# discard (won't throw an error)
set1.discard('c')
set1.discard('b')
set1

# copy
set2 = set1.copy()
set1 == set2 # True
set1 is set2

# Simple set operations:
a={1,2,3,4}
b={4,5,6,7}
a|b # union
a&b # intersection



###########################
# Set comprehensions
{'a' for i in range(10)}  # no duplicates allowed
{i for i in range(10)}
{char for char in 'opportunities' if char in 'aeiou'}  # check which vowels in a string


