/*
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
*/
#include <stdio.h>
#include <stdbool.h>

#define ARRAY_SIZE(array) (sizeof(array) / sizeof(*array))

bool add_up_to (int *piArray, const int iElements, int iNumber)
{
    int iPotentialSolutions[iElements];
    for (int i = 0; i < iElements; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (piArray[i] == iPotentialSolutions[j])
            {
                return true;
            }
        }
        iPotentialSolutions[i] = iNumber - piArray[i];
    }
    return false;
}

int main()
{
    bool result;
    int array1[] = {10,15,3,7};
    result = add_up_to(array1, ARRAY_SIZE(array1), 17); // true
    printf("%d \n", result);

    int array2[] = {10, 2, 8, 9};
    result = add_up_to(array2, ARRAY_SIZE(array2), 32); // false
    printf("%d \n", result);
}