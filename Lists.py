"""In Python, lists are ordered, mutable (changeable) collections that can hold a mix of data types. They are one of the most commonly used data structures in Python."""


a = [1,-1,45,1,2,2,2,2,2,2]

# modifying Lists

# print(a.count(1))
# a.append(6)
# print(a)
# a.insert(1,15)
# print(a)
# a.remove(1)
# print(a)
# a.pop()
# print(a)

# slicing Lists

print(a[1:4])   # Elements from index 1 to 3
print(a[:3])    # First three elements
print(a[::-1])  # Reversed list

# Common List Methods


print(len(a))
print(sum(a))   # Sum (only if all elements are numbers)
print(min(a))    # Minimum value
print(max(a))
print(sorted(a))
a.sort()           # Sort in-place
print(a)
a.clear()          # Removes all elements
print(a)