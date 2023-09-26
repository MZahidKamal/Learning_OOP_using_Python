#-----------------------------------------------------------------------------------------------------------------------
# 2.7 list methods in python
#-----------------------------------------------------------------------------------------------------------------------
# index            0   1   2   3   4   5   6   7   8    9
random_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# -ve Index      -10  -9  -8  -7  -6  -5  -4  -3  -2   -1

print(random_numbers)
#-----------------------------------------------------------------------------------------------------------------------
# Adding a new element into the array.
random_numbers.append(110)
print(random_numbers)
#-----------------------------------------------------------------------------------------------------------------------
# Adding a new element into a specific index position of the array.
random_numbers.insert(1, 15)
print(random_numbers)
#-----------------------------------------------------------------------------------------------------------------------
# Removing a specific element from the array. If the value is not present, it'll show error.
# So we'll check first, and then will use this [.remove()] method.
if 15 in random_numbers:
    random_numbers.remove(15)
print(random_numbers)
#-----------------------------------------------------------------------------------------------------------------------
# Removing the last element of the array.
# Another feature  of this [.pop()] is, it returns the deleted value. So during the deletion, it can also be saved.
popped_value = random_numbers.pop()
print(random_numbers, popped_value)
#-----------------------------------------------------------------------------------------------------------------------
# Finding the index of an element of an array. If the value is not present, it'll show error.
# # So we'll check first, and then will use this [.index()] method.
if 55 in random_numbers:
    index = random_numbers.index(55)
    print(index)
else:
    print('Value not available')
#-----------------------------------------------------------------------------------------------------------------------
# To sort and array in ascending order, we'll use [.sort()] method.
random_numbers = [10, 90, 30, 70, 50, 60, 40, 80, 20, 100]
print(random_numbers)
random_numbers.sort()
print(random_numbers)
#-----------------------------------------------------------------------------------------------------------------------
# To sort and array in descending order, we'll use [.sort() and .reverse()] method.
random_numbers = [10, 90, 30, 70, 50, 60, 40, 80, 20, 100]
print(random_numbers)
random_numbers.sort()
random_numbers.reverse()
print(random_numbers)
#-----------------------------------------------------------------------------------------------------------------------
