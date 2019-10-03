# Lists
# sorted(), .sort(), .extend(), .insert(), [i:i] insertion, del, remove,
# .pop(), .count(), .reverse(), .copy(),

l1 = [4, 4, 5, 2, 7, 5, 5, 1]
l2 = [9, 9, 9]
print('l1', l1)
print('l2', l2)


print('\nsorted(l) (as opposed to l.sort()')
print(sorted(l1))  # [1, 2, 4, 4, 5, 5, 5, 7]
print(l1)  # [4, 4, 5, 2, 7, 5, 5, 1]


print('\nextend (append all elements of another list)')
l1.extend(l2)
print('l1 after extend(l2)', l1)  # [4, 4, 5, 2, 7, 5, 5, 1, 9, 9, 9]


l1 = [4, 4, 5, 2, 7, 5, 5, 1]
print('\n\nl1', l1)
print('\ninsertion')
l1.insert(0, l2)
print('l1 after insert(0, l2)', l1)  # [[9, 9, 9], 4, 4, 5, 2, 7, 5, 5, 1]
l1[3:3] = l2
print('l1 after l1[3:3]=l2', l1)  # [[9, 9, 9], 4, 4, 9, 9, 9, 5, 2, 7, 5, 5, 1]


print('\ndel')
print('l1', l1)
del l1[0:1]
print('l1 after del l1[0:1]', l1)


print('\nremove(item)')  # throws error if not present
print('l1', l1)
print(l1.remove(4))
print('l1 after .remove(4)', l1)



print('\npop(index)')  # returns the popped item
print('l1', l1)
l1.pop()
print('l1 after l1.pop()', l1)
a = l1.pop(0)
print('output of l1.pop(0)', a)
print('l1 after l1.pop(0)', l1)


print('\ncount')
print('l1', l1)
print(l1.count(9))


print('\nreverse')
l1.reverse()
print('l1 after .reverse', l1)


print('\ncopying')
print('don\'t just use =  !!')
print('l1', l1)
l3 = l1
l3.sort()
print('l1 after l3=l1, l3.sort()', l1)  # [2, 5, 5, 5, 7, 9, 9, 9]]

l4 = l1.copy()
l4.reverse()
print('l1 after l4.reverse()', l1)
print('l4', l4)
print('similar results with l4 = l1[:], equivalent to .copy()')

print('\nusing pop in a while loop')
l1 = [1, 2, 3]
l2 = []
while len(l1) > 0:
    print(l1, l2)
    l2.append(l1.pop(0))
