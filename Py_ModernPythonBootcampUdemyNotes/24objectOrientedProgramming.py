# Classes, methods, attributes, instances

# Methods of build-in classes can be found with help():
help(list)

# Why use OOP?  
# Avoiding repetition, representing hierarchical relations of properties
# The difficult part of OOP is deciding which things need their own classes...
# OOP doesn't necessarily use fewer lines of code, but it's better-organized
# Encapsulation and abstraction... more later


#################################
# Creating classes, instances, instance attributes, instance methods

# bare bones, just creating an object in our class:
class tree:
	pass


tree1 = tree()
tree1

# creating an object with a constructor (__init__(self...):)
class Tree:
	def __init__(self):
		print("You planted a tree!")


tree1 = Tree()  # the __init__(self) function will run each time an instance is create



# Instance attributes:
class Tree:
	def __init__(self,name):
		self.name = name
		print("You planted a tree!")


apple_tree = Tree('apple')  # the __init__(self) function will run each time an instance is create
apple_tree.name



# Conventions: underscores (_X, __X, __X__)
# Don't make your own __dunder__ method unless you intend to override an existing one
# Conventionally, _attributes/methods are private and not intended to be called directly on a class object (though no methods/properties are really private in python, unlike in Java)
# Name-mangling with __attributes/methods: can only be accessed by appending an underscore plus the class name before, e.g. '._Tree__attr'


# Methods:
class Tree:
	def __init__(self,name,height):
		self.name = name
		self.height = height 
		print('You planted a tree!')
	def climb(self,height):
		if height > self.height:
			return(f'You climbed the {self.name} tree too high!')
		return(f'You climbed the {self.name} tree up to {height}')	
	def grow(self):
		self.height += 1



help(Tree.climb)
help(Tree.grow)

oak_tree = Tree('oak',39)
oak_tree.height
oak_tree.climb(40)
oak_tree.grow()      # a method that sets the attribute 'height' to a new value
oak_tree.height
oak_tree.climb(40)



#################################
# Creating class attributes and methods 

# One possible use: keeping track of numbers of instances
class Tree:
	grove_size = 3  # a class attribute
	def __init__(self,name,height):
		self.name = name
		self.height = height 
		Tree.grove_size += 1       # modifies the class attribute
		print(f'You planted a(n) {self.name} tree!')
	def climb(self,height):
		if height > self.height:
			return(f'You climbed the {self.name} tree too high!')
		return(f'You climbed the {self.name} tree up to {height}')	
	def grow(self):
		self.height += 1


print(Tree.grove_size)
ash_tree=Tree('ash',25)
print(Tree.grove_size)   # incremented by 1


# Another possible use: validation
class Tree:
	allowed_types = ['oak','ash','beech']
	def __init__(self,name,height):
		if name not in Tree.allowed_types:
			raise ValueError(f"You do not have seeds for a(n) {name} tree")
		self.name = name
		print(f'You planted a(n) {self.name} tree!')
	def climb(self,height):
		if height > self.height:
			return(f'You climbed the {self.name} tree too high!')
		return(f'You climbed the {self.name} tree up to {height}')	
	def grow(self):
		self.height += 1


oak_tree = Tree('oak',39)
Tree.allowed_types  # because this attribute isn't internal to the constructor, it's accessible like this
pine_tree = Tree('pine',100)  # Returns a ValueError as specified
Tree.allowed_types.append('fir')  
fir_tree = Tree('fir',50)  # this is now allowed

# Note that instances of a class have class attributes, but they're just pointing to the class attribute in memory, not unique.
fir_tree.allowed_types
fir_tree.allowed_types is oak_tree.allowed_types # True
id(fir_tree.allowed_types)  
id(oak_tree.allowed_types)
id(Tree.allowed_types)      # All three return the same value





################################
# Class methods (very rarely used)

# use a @decorator
# One use: just for accessing class attributes.
class Tree:
	grove_size = 3
	@classmethod
	def countGrove(cls):
		return Tree.grove_size
	def __init__(self,name,height):
		self.name = name
		Tree.grove_size += 1
		print(f'You planted a(n) {self.name} tree!')
	def grow(self):
		self.height += 1


Tree.countGrove()  
beech_tree = Tree('beech',20)
Tree.countGrove()  # incremented by 1


# Another use for class methods: automatically create instances
class Tree:
	grove_size = 3
	@classmethod
	def plantTrees(cls,file):
		with open(file) as f:
			fl = f.readlines()
		for l in fl:
			name,height = l.split(',') # split the string and unpack it
			cls(name,height)
	def __init__(self,name,height):
		self.name = name
		Tree.grove_size += 1
		print(f'You planted a(n) {self.name} tree!')
	def grow(self):
		self.height += 1


# Now this class method allows us to create instances from a file
Tree.plantTrees('/Users/davidrogers/Documents/gitHub/References-and-Illustrations/Py_UdemyNotes/tree_class_method_example.txt')



#####################################
# the dunder method __repr__
class Tree:
	def __init__(self,name,height):
		self.name = name
		self.height = height
		print(f'You planted a(n) {self.name} tree!')

oak_tree = Tree('oak',5)
oak_tree # just returns <__main__.Tree object at 0x10b28d7f0>

# We can customize the representation of class instances with the __repr__ method:

class Tree:
	def __init__(self,name,height):
		self.name = name
		self.height = height
		print(f'You planted a(n) {self.name} tree!')
	def __repr__(self):
		return(f'This {self.name} tree has a height of {self.height}')

alder_tree = Tree('alder', 45)
alder_tree  # returns 'This alder tree has a height of 45'



