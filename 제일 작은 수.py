def solution(arr):
    temp_arr = arr.copy()
    arr.sort()
    min_value = arr[0]
    arr.pop(0)
    if arr :
        temp_arr.pop(temp_arr.index(min_value))
        return temp_arr
    else :
        return [-1]