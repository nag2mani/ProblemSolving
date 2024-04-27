def has_integer_greater_than_one(lst):
    for item in lst:
        if isinstance(item, int) and item > 1:
            return True
    return False
my_list = [0, 1, 2, 3, 4, -2, 2]
print(has_integer_greater_than_one(my_list))  # Output: True

my_list = [0, 1, -2, -3, -4]
print(has_integer_greater_than_one(my_list))  # Output: False

my_list = [0, 1, 'a', 'b', 3]
print(has_integer_greater_than_one(my_list))  # Output: True
