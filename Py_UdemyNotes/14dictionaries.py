# Dictionaries
d={'key1':1,'key2':2}
dl={'key3':[1,2],'key4':[3,4]}
dd={'dict1':{'key5':1,'key6':2},'dict2':{'key7':3,'key8':4}}

# Dictionaries are most useful for associating general attributes and their specific values.
# Note that the order of keys in a dictionary is not set as it is with lists indexes

# Using dict() somewhat simplifies manual dictionary creation
monster1 = dict(fangs=2,color='blue')
monster1


###########################
# Accessing dictionary values (unlike with lists, we use a key rather than an index)
monster1['fangs']
monster1['name'] # key error
a=f'This monster has {monster1["fangs"]} fangs and is {monster1["color"]}'
a

# Iterating through dictionaries:

# Values: the .values() method returns an iterable set of values
monster1.values()
print(type(monster1.values()))
for v in monster1.values():
	print(v)


# Keys:
monster1.keys()
print(monster1.keys())
for k in monster1.keys():
	print(k)


# Both keys and values: returns a list of tuples if only a single index specified
monster1.items()
for i in monster1.items():
	print(i)


# Or if two indexes given (tuple unpacking):
for k,v in monster1.items():
	print(f'key is {k} and value is {v}')


# Checking for the existence of a given key (without getting a key error):
'fangs' in monster1
'color' in monster1.keys() # equivalent (the default behavior for 'in' with dictionaries)
'wings' in monster1 # our dictionary doesn't contain information about whether monster1 has wings

# Checking for the existence of a given value: we need to specify .values()
'blue' in monster1.values()



###########################
# Some dictionary methods:
numbers = {
'evens':[i for i in range(10) if i%2==0]
,'odds':[i for i in range(10) if i%2!=0]}


# .copy()
more_numbers=numbers.copy()
more_numbers
more_numbers==numbers   # the two dictionaries have the same keys and values...
more_numbers is numbers   # but they're distinct objects in memory
# more_numbers = numbers
# more_numbers is numbers  # now they're the same object in memory

# .clear() empties out all keys and values
more_numbers.clear()

# .fromkeys() a way to add to (or create) a dictionary (in addition to {}=... or dict()):
# takes two argumens and extracts keys and values 
# by treating the first as an iterable and the second as the value
# Useful for creating many keys with a single default value
fr1={}.fromkeys('k',[1,2,3]) # {'k':[1,2,3]}
fr1
fr2={}.fromkeys('keys',[1,2,3])  # {'k':[1,2,3],'e':...}
fr2
fr3={}.fromkeys(['key1','key2'],[1,2,3])  # {'key1:[1,2,3],...}
fr3 

# get() gets value for a key without throwing a key error (just None)
numbers.get('evens')
numbers.get('primes')

if numbers.get('primes'):
	print('we have prime info')
else:
	print('sorry, no prime info')


# pop() and popitem()  - similar to removing an item from a list, except with a key
numbers = {
'evens':[i for i in range(10) if i%2==0]
,'odds':[i for i in range(10) if i%2!=0]}
morenumbers=numbers.copy()
morenumbers.pop() # in a list, this removes the last item; but dictionaries lack order
morenumbers.pop('evens')
morenumbers  # just odds left

morenumbers=numbers.copy()
morenumbers.popitem() # removes a random key-value pair
morenumbers


# update() method takes another dictionary as an argument and adds it, overwriting shared keys

numbers = {
'evens':[i for i in range(10) if i%2==0]
,'odds':[i for i in range(10) if i%2!=0]}
numbers['yetmore']=[1,1,1] # first, a simple way to add key-value pairs one at a time
numbers

numbers
othernumbers=dict(primes=[2,3,5],squares=[1,4,9],evens=[0,2,4,6,8,10,12,14,16])
numbers.update(othernumbers)
numbers # primes and squares have been added, evens has been overwritten































