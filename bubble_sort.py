from selection_sort import swap

def sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

if __name__ == "__main__":
    arr = [2, 1, 9, 6, 4, 5, 0]
    sort(arr)
    print(arr)