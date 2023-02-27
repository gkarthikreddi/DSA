# Comparing element with previous elements and placing it in the right position
def insert(arr, left_idx, value):
    for i in range(left_idx, -1, -1):
        if arr[i] > value: 
            arr[i+1] = arr[i]
            left_idx -= 1
        arr[left_idx + 1] = value

def sort(arr):
    for i in range(1, len(arr)):
        insert(arr, i-1, arr[i])

if __name__ == "__main__":
    arr = [5, 8, 2, 1, 66, 33, 4]
    sort(arr)
    print(arr)