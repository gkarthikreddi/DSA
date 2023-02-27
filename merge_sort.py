def sort(arr):
    # Dividing list into sublists
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        # Recursively calling to divide into sublists length of one
        sort(left_arr)
        sort(right_arr)
        # Comparing both sublists and arranging them in order
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr): 
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

if __name__ == "__main__":
    arr = [6, 2, 7, 3, 22, 19, 56]
    sort(arr)
    print(arr)