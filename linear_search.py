# Looping through every element
def search(arr, value):
    for i in arr:
        if i == value: return arr.index(i)
    return -1

if __name__ == "__main__":
    arr = [3, 4, 66, 14, 1, 90, 2]
    print(search(arr, 1))