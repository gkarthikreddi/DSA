from selection_sort import swap

def sort(arr):
    if len(arr) > 1:
        pivot = arr[-1]
        j = 0
        for i in range(len(arr)):
            if arr[i] <= pivot:
                swap(arr, i, j)
                j += 1
        idx = arr.index(pivot)
        arr[:idx] = sort(arr[:idx])
        arr[idx+1:] = sort(arr[idx+1:])
    return arr

if __name__ == "__main__":
    arr = [5, 66, 23, 1, 4, 17, 2]
    sort(arr)
    print(arr)