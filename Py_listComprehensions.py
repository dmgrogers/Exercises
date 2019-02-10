# List comprehensions from the ground up:
[1 for i in range(5)] # repeating an element
['abcdefghijklmnop'[:n] for n in range(10)] # extending a string
[i for i in range(5)] # sequence
[i for i in range(5) if i%2==0] # condition on a sequence
[i for i in [6,3,8,5,6,9] if i%3==0] # condition on a list
[i for i in 'abcdefg' if i in 'aeiou'] # condition on a string
[i*2 for i in 'hello world' if i not in 'aeiou']
[[i for i in range(3)] for n in range(3)] # nested independent list comprehensions
[[i for i in range(n)] for n in range(1,5)] # nested dependent lc's


############################
# Some exercises from Udemy:

# Get the first letter of each item in this list:
l=["Ellie","Time","Matt"]

# A one-off iteration with append:
answer3=[]
for e in l:
answer3.append(e[0])
answer3

# A general function taking any list as an argument:
def getFirst(ls):
    nl=[]
    for e in ls:
        nl.append(e[0])
    return nl

answer=getFirst(l)
answer

# Or, a list comprehension:
answer1=[e[0] for e in l]
answer1




# List comprehension with a condition:
# Get all multiples of 2:
answer2=[e for e in list(range(10)) if e%2==0]
answer2

# Intersection of two lists:
l1=[1,2,3,4]
l2=[3,4,5,6]
answer4=[e for e in l2 if e in l1]
answer4

# Reverse a list of strings and convert to lower case
l=["Ellie","Time","Matt"]
answer5=[i[::-1].lower() for i in l] # [::-1] slice beginning to end in reverse
answer5

# Iterable with given list of elements removed:
a='amazing'
answer7 = [l for l in list('amazing') if not l in ['a','e','i','o','u']]
answer7
# But you can also use 'in' with strings:
answer7 = [l for l in list('amazing') if l not in 'aeiou']




# Nested list comprehensions
# use a nested list comprehension to get [[1,2,3],[1,2,3]]:
# The key is that the first part of the comprehension can be a list comp,
# And the second can be just an iterable (not a condition or a pre-exiting list)
[[i for i in range(1,4)] for n in range(3)]




