def qs_pivot(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr) // 2]
    L = [x for x in arr if x < pivot]   
    R = [x for x in arr if x > pivot]
    M = [x for x in arr if x == pivot] 
    return qs_pivot(L) + M + qs_pivot(R)
if __name__ == "__main__":
    arr = [28, 11, 2, 88, 0, 18, 99]
    print("Original array:", arr)
    sort_arr = qs_pivot(arr)
print("Sorted array:", sort_arr)
