/**
* Given an array of integers, return a new array such that each element at index i of the new array is the product of all
* the numbers in the original array except the one at i.
*
* For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
* If our input was [3, 2, 1], the expected output would be [2, 3, 6].
*
* Follow-up: what if you can't use division?
**/

#include <stdio.h>

void product_of_all_numbers_division(int *inputArray, int size, int *outputArray)
{
    int product = 1;
    for(int i = 0; i < size; i++){
        product *= inputArray[i];
    }

    for(int i = 0; i < size; i++){
        outputArray[i] = product / inputArray[i];
    }
}

// without division
void product_of_all_numbers(int *inputArray, int size, int *outputArray)
{
    int product;
    for(int i = 0; i < size; i++)
    {
        product = 1;
        for(int j = 0; j < size; j++){
            if( i == j) continue;
            product *= inputArray[j];
        }
        outputArray[i] = product;
    }
}

int main()
{
    int inputArray[] = {1, 2, 3, 4, 5};
    int arraySize = 5;
    int outputArray[arraySize];

    product_of_all_numbers(inputArray, arraySize, outputArray);

    for(int i = 0; i < arraySize; i++){
        printf("%d \n", outputArray[i]);
    }
}
