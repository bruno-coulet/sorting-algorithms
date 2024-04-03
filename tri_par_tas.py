def tri_par_tas(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        tri_par_tas(arr, n, largest)

def tri_tas(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        tri_par_tas(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        tri_par_tas(arr, i, 0)
    return arr
