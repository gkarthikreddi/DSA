from selection_sort import swap

# Largest element of the list will be at the 0th index
def heapify(arr):
    # Parent of the leaf node: ((i-1)/2)
    i = (len(arr)-2)//2
    while i > -1:
        left_child = 2*i + 1
        right_child = 2*i + 2
        try:
            if arr[left_child] > arr[i]:
                swap(arr, left_child, i)
            if arr[right_child] > arr[i]:
                swap(arr, right_child, i)
        except:
            i -= 1
            continue
        i -= 1
    return arr

def sort(arr):
    end = len(arr) - 1
    heapify(arr)
    while end:
        swap(arr, 0, end)
        arr[:end] = heapify(arr[:end])
        end -= 1

if __name__ == "__main__":
    arr = [19, 25, 3, 22, 11, 10, 7, 8, 6]
    sort(arr)
    print(arr)