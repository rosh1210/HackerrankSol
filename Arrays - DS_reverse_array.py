


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
