# slicing
a = 'abcdefgabc'
# print(a[-1])
# print(a[-3:])
print('This is a:', a)

print('\nfind')
print(a.find('ab', 0, 1))
print(a.find('ab', 0, 2))

print('\ncount')
print(a.count('a'))  # 2

print('\nendswith')
print(a.endswith('efg'))  # False
print(a.endswith('efg', 0, -3))  # True


print('\nisalnum')
print(a.isalnum())


b = '  quick brown \n fox  '
print('This is b:', b)

print('\nsplit')
print(b.split())
print(b.split('\n'))


print('\nstrip')
print(b)
print(b.lstrip())


print('\nisidentifier')
print('abc', 'abc'.isidentifier())
print('2abc', '2abc'.isidentifier()) # 2abc False
print(' hi ', ' hi '.isidentifier())


print('\npartition')  # returns tuple
print(a.partition('b'))  #('a', 'b', 'cdefgabc')
print(a.partition('x'))



# Find indexes of all occurrences of a substring:
def find_all(s, substring):
    indexes = []
    start = 0
    if len(substring) == 0:
        print('empty substring')
        return indexes
    while substring in s:
        i = s.find(substring)
        indexes.append(i + start)
        start += i + len(substring)
        s = s[(i + len(substring)):]
    return indexes


assert(find_all('aa', 'a') == [0, 1])
assert(find_all('abcab', 'ab') == [0, 3])
assert(find_all('', '') == [])





