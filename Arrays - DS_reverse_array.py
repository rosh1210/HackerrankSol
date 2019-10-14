'''An array is a type of data structure that stores elements of the same type in a contiguous block of memory.
In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as 
(you may also see it written as ).
Given an array, , of  integers, print each element in reverse order as a single line of space-separated integers.'''

'''Method-1:- arr.reverse()
   Method-2:- while start < end:
               a = arr[start]
               arr[start] = arr[end]
               arr[end] = a '''

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a,n):

    start = 0
    end = n - 1
    while start < end:

        a[start], a[end] = a[end], a[start]
        start = start + 1
        end = end - 1

    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr,arr_count)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
