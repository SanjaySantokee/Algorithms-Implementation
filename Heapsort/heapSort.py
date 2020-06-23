"""
    /*
        Full Name: Sanjay Santokee
        Email: sanjay.santokee@my.uwi.edu
    */  
"""

# (a)
def heapSort(a: list):
    # finding the length of array a, 1 is subtracted because of the array being indexed at 1
    n = len(a) - 1

    # building a max heap with the makeHeap function on array a
    makeHeap(a, n)

    for j in range(n, 1, -1):
        # Swaps the first and last numbers (from the unsorted array)
        a[1], a[j] = a[j], a[1]
        # Calls siftDown to place the number at the top of the heap to its right position
        siftDown(a, j - 1, 1)

    # This removes the dummy value of -1 placed at the start of the array (index position 0)
    a.pop(0)
    return a


# (b)
def makeHeap(a: list, n: int):
    # setting the variable r to be the length of the array n
    r = n

    # For loop that runs from half of the array down to 1
    # (specified as 0 because of python's range function)
    for i in range(n // 2, 0, -1):
        siftDown(a, r, i)  # siftDown called on the array to make it a max heap


# (c)
def siftDown(a: list, r: int, i: int):
    # boolean variable to stop while loop
    done = False

    j = 2 * i  # left child a[j] of parent a[i]
    while not done and j <= r:
        if j < r and a[j] < a[j + 1]:  # finding index of maximum value between a[j] and a[j+i]
            j = j + 1
        if a[i] < a[j]:  # if parent a[i] < left child a[j] and right child a[j+1]
            a[i], a[j] = a[j], a[i]
            i = j  # update current parent node a[i]
            j = 2 * j  # update left child of a[j] of current parent a[i]
        else:
            done = True


if __name__ == '__main__':
    # Creating an array, a, with the first value being -1 since the algorithm is using indexes at position 1
    a = [-1]

    # Reading in input from the 'heapsort.txt' input file and adding the numbers to the list
    with open('heapsort.txt') as file:
        for line in file:
            a.append(int(line.strip('\n')))

    print('Heap Sorting: ')
    print('Input (unsorted array): ', a[1:])

    # Calling the heapSort function on the array a and collecting the sorted array in heap_sorted_a
    heap_sorted_a = heapSort(a)
    print('Output (heap sorted array): ', heap_sorted_a)
