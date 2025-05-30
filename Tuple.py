"""In Python, a tuple is an ordered, immutable collection of elements. That means once a tuple is created, its contents cannot be changed."""


'''defined in ()
allow diff types of elements
allow duplicates
allow index and slicing
immutable
no methods we can use builtins'''

# Empty tuple
t1 = ()

# Tuple with elements
t2 = (1, 2, 3)

# Tuple with mixed data types
t3 = (1, "abhi", 3.14, True)

# Tuple without parentheses (Python allows this)
t4 = 1, 2, 3

# Single-element tuple (note the comma)
t5 = (5,)

#Immutability Example
a = (1,2,3)
#a[1] = 3  #type error

#Tuple Packing and Unpacking

# Packing is the process of putting multiple values into a single tuple.
person = ("Abhinav", 25, "Engineer")

# Unpacking means extracting the values from a tuple and assigning them to individual variables.
name, age, profession = person
print(name)       # Abhinav
print(age)        # 25

#lcnejbvweiub
# Tuple operations
b = (1,2,2,4,4,5,6,"abhi")
print(len(b))
print(b.count(2))
print(b.index(2))  # Index of value 3