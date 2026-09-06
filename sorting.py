arr = [7, 2, 5, 1, 3, -5, 4, -1]

# bubble sort: t-> O(n*n) s-> O(1) inplace
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    print(f"Bubble Sort: {arr}")

bubble_sort(arr.copy())

# insertion sort: t-> O(n*n) s-> O(1)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    print(f"Insertion Sort: {arr}")

insertion_sort(arr.copy())

# selection sort: t-> O(n*n) s-> O(1)
def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                break

    print(f"Selection Sort: {arr}")

selection_sort(arr.copy())

# merge sort: t-> O(n log n) s-> O(n)
def merge_sort(lst):
    ln = len(lst)

    if ln <= 1:
        return lst

    mid = ln // 2

    left = lst[:mid]
    right = lst[mid:]

    L = merge_sort(left)
    R = merge_sort(right)

    n_lst = [0] * ln
    i, l, r = 0, 0, 0

    while l < len(left) and r < len(right):
        if L[l] < R[r]:
            n_lst[i] = L[l]
            l += 1
        else:
            n_lst[i] = R[r]
            r += 1

        i += 1

    while l < len(left):
        n_lst[i] = L[l]
        l += 1
        i += 1

    while r < len(right):
        n_lst[i] = R[r]
        r += 1
        i += 1

    return  n_lst

print("----------Merge Sort----------")

my_list = [38, 27, 43, 3, 9, 82, 9, 10]
print("Before sorting:", my_list)

my_new_list = merge_sort(my_list)
print("After sorting:", my_new_list)

# quick sort t: O(N log N)/O(N*N) in worst case if list is already sorted - s: O(N)
def partition(arr, low, high):
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def quick_sort(arr, low, high):
    if len(arr) <= 1:
        return  arr

    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, pi+1, high)

        quick_sort(arr, low, pi-1)

print("----------Quick Sort----------")

my_list = [38, 27, 43, 3, 9, 82, 9, 10]
print("Before sorting:", my_list)

quick_sort(my_list, 0, len(my_list)-1)
print("After sorting:", my_list)