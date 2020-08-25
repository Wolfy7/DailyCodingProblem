'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def add_up_to(array, k):
    potential_solutions = set()
    for num in array:
        if num in potential_solutions:
            return True
        potential_solutions.add(k-num)
    return False

print(add_up_to([10,15,3,7], 17))   # True
print(add_up_to([10, 2, 8, 9], 32)) # False