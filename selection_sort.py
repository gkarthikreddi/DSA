# Swaping two elements
def swap(arr, first_idx, second_idx):
    temp = arr[first_idx]
    arr[first_idx] = arr[second_idx]
    arr[second_idx] = temp

# Finding the index of least element in the sublist
def min_index(arr, start_idx):
    for i in range(start_idx, len(arr)):
        if arr[i] <= arr[start_idx]: start_idx = i
    return start_idx

def sort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[min_index(arr, i+1)]:
            swap(arr, i, min_index(arr, i+1))

if __name__ == "__main__":
    arr = [6, 3, 8, 11, 1, 55, 99]
    sort(arr)
    print(arr)