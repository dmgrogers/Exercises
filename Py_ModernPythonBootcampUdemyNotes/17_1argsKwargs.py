# *args and *kwargs


def fancy(*args):
    print('fancy')
    for i in args:
        print('*^*^*' + i + '*^*^*')



fancy('a', 'b')
l = ['a', 'b']
fancy(*l)


# Defining a function for when you may want to pass an indeterminate number
# of keyword arguments

def more_fancy(**kwargs):
    print('more_fancy')
    for k, v in kwargs.items():
        print('~~' + k + '~~' + str(v) + '~~')



more_fancy(a=1, b='2')
d = {'a': 1, 'b': '2'}
more_fancy(**d)


# Or, this is less flexible but convenient
def yet_more_fancy(a, b):
    print('~*~'+str(a)+'~*~')
    print('*~*'+str(b)+'*~*')


yet_more_fancy(**d)
