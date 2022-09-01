def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    subMax = max(arr[1:])
    return arr[0] if arr[0] > subMax else subMax

array = [1,9,2,3,4,5,8]
print(max(array))    