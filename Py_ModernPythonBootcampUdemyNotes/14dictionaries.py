# Dictionaries:
# dict, assignment, [], get, values, keys, items,
# in, copy, is, clear, fromkeys, pop, popitem, update

d = {'key1': 1, 'key2': 2}
dl = {'key3': [1, 2], 'key4': [3, 4]}
dd = {'dict1': {'key5': 1, 'key6': 2}, 'dict2': {'key7': 3, 'key8':4 }}

# Note that the order of keys in a dictionary is not set as it is with lists indexes

# Using dict() somewhat simplifies manual dictionary creation
monster1 = dict(fangs=2, color='blue')
print('monster1', monster1)
monster1 = dict([('fangs', 2), ('color', 'blue')])  # list of items
monster1['tail'] = 'yes'
print('monster1', monster1)


###########################
# Accessing dictionary values (unlike with lists, we use a key rather than an index)
print(monster1['fangs'])
# monster1['name'] # key error
print(f'This monster has {monster1["fangs"]} fangs and is {monster1["color"]}')


# Iterating through dictionaries:
# Values: the .values() method returns an iterable set of values
print('\nvalues()', list(monster1.values()))


# Keys:
print('\nkeys', list(monster1.keys()))


# Both keys and values: returns a list of tuples if only a single index specified
print('\nitems', list(monster1.items()))


# Or if two indexes given (tuple unpacking):
for k, v in monster1.items():
	print(f'key is {k} and value is {v}')


print('\nChecking for existence of a key (or value)')
print('\nin')
print('fangs' in monster1)
print('color' in monster1.keys())  # equivalent (the default behavior for 'in' with dictionaries)
print('wings' in monster1)  # our dictionary doesn't contain information about whether monster1 has wings

# Checking for the existence of a given value: we need to specify .values()
print('blue' in monster1.values())



###########################
# Some dictionary methods:
numbers = {'evens': [i for i in range(10) if i % 2 == 0],
			'odds': [i for i in range(10) if i % 2 != 0]
}


# .copy()
more_numbers = numbers.copy()
print(more_numbers)
print(more_numbers == numbers)  # the two dictionaries have the same keys and values...
print(more_numbers is numbers)   # but they're distinct objects in memory
# more_numbers = numbers
# more_numbers is numbers  # now they're the same object in memory

# .clear() empties out all keys and values
more_numbers.clear()

# .fromkeys() a way to add to (or create) a dictionary (in addition to {}=... or dict()):
# takes two argumens and extracts keys and values 
# by treating the first as an iterable and the second as the value
# Useful for creating many keys with a single default value
print('\nfromkeys')
fr1 = {}.fromkeys('k', [1, 2, 3]) # {'k':[1,2,3]}
print('fromkeys', fr1)
fr2 = {}.fromkeys('keys', [1, 2, 3])  # {'k':[1,2,3],'e':...}
print('fromkeys', fr2)
fr3 = {}.fromkeys(['key1', 'key2'], [1, 2, 3])  # {'key1:[1,2,3],...}
print('fromkeys', fr3)

# get() gets value for a key without throwing a key error (just None)
numbers.get('evens')
numbers.get('primes')

if numbers.get('primes'):
	print('we have prime info')
else:
	print('sorry, no prime info')


print('\nWe can pop items in a dictionary by key')
# pop() and popitem()  - similar to removing an item from a list, except with a key
numbers = {
			'evens': [i for i in range(10) if i%2 == 0],
			'odds': [i for i in range(10) if i%2 != 0]
}
print('numbers', numbers)
# morenumbers.pop() # in a list, this removes the last item; but dictionaries lack order
numbers.pop('evens')
print('numbers after pop(\'evens\')', numbers)  # just odds left




# update() method takes another dictionary as an argument and adds it, overwriting shared keys
print('\nupdate (though for single values just assigning the new key works fine')
numbers = {
		'evens': [i for i in range(10) if i % 2 == 0],
		'odds': [i for i in range(10) if i % 2 != 0]
}
numbers['yetmore'] = [1, 1, 1]  # first, a simple way to add key-value pairs one at a time
print(numbers)

othernumbers = dict(primes=[2, 3, 5], squares=[1, 4, 9], evens=[0, 2, 4, 6, 8, 10, 12, 14, 16])
numbers.update(othernumbers)
print(numbers) # primes and squares have been added, evens has been overwritten


print('\nnumbers', numbers)
print('what kind of a number is 5?')
print({k: v for k, v in numbers.items() if 5 in v})





























