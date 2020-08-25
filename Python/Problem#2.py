"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_of_all_numbers_division(array):
    new_array = list()
    product = 1

    for num in array:
        product *= num

    for num in array:
        new_array.append(int(product / num))

    return new_array


# without division
def product_of_all_numbers(array):
    new_array = list()

    for i in enumerate(array):
        product = 1
        for k, num in enumerate(array):
            if i[0] == k: continue
            product *= num
        new_array.append(product)

    return  new_array


print(product_of_all_numbers_division([1, 2, 3, 4, 5]))
print(product_of_all_numbers_division([3, 2, 1]))

print(product_of_all_numbers([1, 2, 3, 4, 5]))
print(product_of_all_numbers([3, 2, 1]))
