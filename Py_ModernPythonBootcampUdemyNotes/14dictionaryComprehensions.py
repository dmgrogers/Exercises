# Similar to list comprehensions
evens=dict(first=0,second=2,third=4,fourth=6) # starter dictionary

# From the ground up
{'a':i for i in [1,2,3]} # assigns the last value in the list to key 'a'
{i:i for i in [1,2,3]} # assigning keys and values based on a single list
{i:i**3 for i in [1,2,3]}
{'a'*i:i**3 for i in [1,2,3]}
{'abc'[i]:'xyz'[i] for i in range(len('abc'))}
{k:v for k,v in evens.items()} # assigning keys and values independently based on another dict
{k+'_squared':v**2 for k,v in evens.items()} 
{n:('triple' if n%3==0 else 'nontriple') for n in range(1,100)}  # conditional value assignment
{(k.upper() if k is 'first' else k):v for k,v in evens.items()} # conditional key based on key
{(k.upper() if v%3==0 else k):v for k,v in evens.items()} # conditional key based on value


# Exercises: given a list of two-item lists, make a dictionary
person = [['name','alice'],['job','artist']] # convert to a dictionary in the reasonable way
{l[0]:l[1] for l in person} # one way, using list indexes
{l0:l1 for l0,l1 in person} # using unpacking
dict(person) # simplest of all! Given a list of pairs, dict() makes a dictionary

# create a dictionary like {'a':0,'e':0, 'i':...}
{k:0 for k in 'aeiou'}
{}.fromkeys('aeiou',0)

# create a dictionary mapping ascii codes 32 to 126:
{i:chr(i) for i in range(32,127)}
