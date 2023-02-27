from quick_sort import sort

# Arrays should be sorted before performing binary search
def search(arr, low, high, value):
    if high >= low:
        mid = (high + low + 1) // 2
        if arr[mid] == value:
            return mid
        elif value > arr[mid]:
            return search(arr, mid+1, high, value)
        else:
            return search(arr, low, mid-1,  value)
    return -1


if __name__ == "__main__":
    arr = [2, 33, 5, 1, 16, 10, 12]
    sort(arr)
    print(arr)
    print(search(arr, 0, len(arr)-1, 12))