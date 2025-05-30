"""A string in Python is a sequence of characters. It is an immutable data type, meaning that once a string is created, its value cannot be changed.
   Strings are used to represent text and are enclosed in either single quotes, double quotes, or triple quotes."""


 # creating strings 
 
name = "Abhi" 
a = "Hello"
b = '''this is a multiline
       string'''

# string length

a = "Abhinav"
print(len(a))

# Accessing Characters (Indexing & Slicing)

s = "python"
print(s[1])
print(s[4])
print(s[1:5])

# String Methods

a = "noveltronix PVT LTD"
print(a.upper())
print(a.capitalize())
print(a.replace("PVT" , "company"))
print(a.split())
print(a.find("t"))

# Concatenation and Repetition
a = "Abhinav"
b = "Varma"
print(a + " " + b)
print(a * 5)


# String membership

'''String membership in Python involves checking if a substring exists within a larger string. Python provides two membership operators for this purpose: 
in and not in. 
in operator:
 Returns True if the substring is found within the string, and False otherwise.
not in operator:
 Returns True if the substring is not found within the string, and False otherwise.'''

name = "Abhinav raju"

print("raju" in name)
print("hello" in name)
print("Abhinav" in name)


#  f-Strings (Formatted Strings)

name = "Raju"
age = 25
print(f"my name is {name},i am {age} year old")
print("my name is {},i am {} year old.".format(name,age))


#  String Comparison

a = "Apple"
b = "apple"
print(a != b)
print(a == b)

a = 10
b = 15
print(a < b)
print(a > b)


