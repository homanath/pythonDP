## List operations in Python
## Lists are mutable sequences, typically used to store collections of homogeneous items.(it work as array in other languages)
# Creating a list
list = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list)
# Accessing elements in a list
list.append(23)
print(list)
# Inserting an element at a specific position
list.insert(4, 22)
print(list)
# Removing an element from a list
list.remove(10)
print(list)
# Removing an element by index
del list[11]
print(list)
# Popping an element from the end of the list
list.pop()
print(list)
list.pop(2)
print(list)
# printing the length of the list
print(len(list))
# printing the value at a specific index
print(list[2])
# # Slicing a list
# print(list[2:5])  # from index 2 to 4
