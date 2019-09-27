# Built-in functions
# all, any, bin, eval, filter, map, hash, help, min, open, reversed

all_any = [True, False]
print(all(all_any))
print(any(all_any))  # True

print(bin(0))
print(bin(9))  # 0b1001
print(bin(10000))


eval('print(5)')

l = [4, 5, 6]
l1 = list(filter(lambda x: x > 5, l))
print(l1)                               # [6]
l2 = list(map(lambda x: x > 5, l))
print(l2)                               # [False, False, True]


print(hash('abc132'))
print(help(hash))

print(min(l))

with open('test_file.txt', 'w') as f:
    f.write('new content overwriting old')
with open ('test_file.txt', 'r') as f:
    out = f.read()
print('now file reads', out)

l = list(range(10))
print(list(reversed(l)))  # note diff vs sorted
print(l)


