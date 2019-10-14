'''An array is a type of data structure that stores elements of the same type in a contiguous block of memory.
In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as 
(you may also see it written as ).
Given an array, , of  integers, print each element in reverse order as a single line of space-separated integers.'''

'''Method-1:- arr.reverse()
   Method-2:- while start < end:
               a = arr[start]
               arr[start] = arr[end]
               arr[end] = a '''

#arr.reverse()
#print(arr)
#/reversing the array
#for i in range(n):
 #   print(arr)
  #  print()

def reverse(a):
    start = 0
    end = n - 1
    while start < end:
        # a = arr[start]
        # arr[start] = arr[end]
        # arr[end] = a

        a[start], a[end] = a[end], a[start]
        start = start + 1
        end = end - 1

    print(a)
if __name__ == '__main__':
    n = int(input("Enter the size of the array\n"))
    arr = []
    for i in range(n):
        arr.append(int(input()))
    #print(arr)
    reverse(arr)
