#-----------------------------------------------------------------------------------------------------------------------
# 3.3 Set and set methods in python
#-----------------------------------------------------------------------------------------------------------------------
# Set items are unordered, unchangeable, and do not allow duplicate values.
# x = {"apple", "banana", "cherry"}

# Let's create a list of numbers and then print it.
random_numbers = [12, 56, 98, 78, 56, 12, 6, 98]
print(random_numbers)
print(type(random_numbers))
#-----------------------------------------------------------------------------------------------------------------------
# Now let's convert it into a Tuple and print.
random_numbers_tuple = tuple(random_numbers)
print(random_numbers_tuple)
print(type(random_numbers_tuple))

# In the above code, see the changes in the output.
# After converting to set, () came instead of [].
#-----------------------------------------------------------------------------------------------------------------------
# Now let's convert it into a Set and print.
random_numbers_set = set(random_numbers)
print(random_numbers_set)
print(type(random_numbers_set))

# In the above code, see the changes in the output.
# After converting to set, {} came instead of [], and all duplicate are removed.
#-----------------------------------------------------------------------------------------------------------------------
random_numbers_set.add(55)
print(random_numbers_set)

# In the above code, we've added a number into the set and printed it.
# See the output, the new element is added and already sorted.
#-----------------------------------------------------------------------------------------------------------------------
random_numbers_set.remove(78)
print(random_numbers_set)

# In the above code, we've removed a number from the set and printed it.
# See the output, after removing element it's still sorted.
#-----------------------------------------------------------------------------------------------------------------------
for num in random_numbers_set:
    print(num)
#-----------------------------------------------------------------------------------------------------------------------
A = {1, 3, 5, 7, 9}
B = {1, 2, 3, 4, 5}
print(A & B)
print(A | B)

# The above code is printing only the elements which is common in both A and B.
#-----------------------------------------------------------------------------------------------------------------------
