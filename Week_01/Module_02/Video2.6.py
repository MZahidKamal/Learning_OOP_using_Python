#-----------------------------------------------------------------------------------------------------------------------
# 2.6 List, List index fun and slice in python
#-----------------------------------------------------------------------------------------------------------------------
# List / array / collection, are almost same, but with different name in different programming languages.
# Python maintains two index systems. One is regular indexing, another one is negative indexing.

# index            0   1   2   3   4   5   6   7   8    9
random_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# -ve Index      -10  -9  -8  -7  -6  -5  -4  -3  -2   -1

print(random_numbers[3], random_numbers[-7])
print(random_numbers[3], random_numbers[-3])
#-----------------------------------------------------------------------------------------------------------------------
# Printing a list based on a given range.
# It strats from the given start index, and will stop before the given end index.
# Combination of regular index and -ve index is also possible.

print(random_numbers[2:7])
print(random_numbers[-8:-3])
print(random_numbers[2:-3])
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same thing again, but this time using intervals.

print(random_numbers[1:9:1])
print(random_numbers[-9:-1:2])
print(random_numbers[1:-1:3])

# Initially with 1 interval, then 2 intervals, and then at the end 3 intervals.
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same thing again, but this time from reverse direction.

print(random_numbers[9:1:-1])
print(random_numbers[-1:-9:-2])
print(random_numbers[9:-9:-3])

# Initially with 1 interval, then 2 intervals, and then at the end 3 intervals.
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same thing again, but this time more shortly.

print(random_numbers[4:])
print(random_numbers[:-6])
print(random_numbers[:])

# First one will print starting from index 4 and will go till the end.
# Second one will print starting from beginning and will go till the index -6.
# Third one will print starting from beginning and will go till the end index, as starting and ending is not mentioned.
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same thing again, but this time we'll print the complete array in reverse order, and shortly.
print(random_numbers[::-1])
#-----------------------------------------------------------------------------------------------------------------------
# There are some very important built in methods to handle List is Python. Visit, read and practice them.
"""
list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position.

list.remove(x)
Remove the first item from the list whose value is equal to x.

list.pop([i])
Remove the item at the given position in the list, and return it.
If no index is specified, a.pop() removes and returns the last item in the list.

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation.

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].

An example that uses most of the list methods:
"""
# To Learn more, visit (https://docs.python.org/3/tutorial/datastructures.html).
#-----------------------------------------------------------------------------------------------------------------------
